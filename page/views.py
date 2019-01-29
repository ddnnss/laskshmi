from django.shortcuts import render
from .models import Banner
from item.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from customuser.forms import SignUpForm, UpdateForm
from order.models import *
from cart.models import Cart
from customuser.models import Guest


def about_us(request):
    return render(request, 'page/about_us.html', locals())


def contacts(request):
    return render(request, 'page/contacts.html', locals())


def dostavka(request):
    return render(request, 'page/dostavka.html', locals())


def new(request):
    items = Item.objects.filter(is_new=True)
    return render(request, 'page/new.html', locals())


def checkout(request):

    if request.POST:
        if request.POST.get('form_type') == 'user_info':
            client = request.user
            mail_tmp = client.is_allow_email
            form = UpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                client.profile_ok = True
                client.is_allow_email = mail_tmp
                client.save(force_update=True)

                return render(request, 'page/checkout.html', locals())
            else:
                client = request.user
                form = UpdateForm(instance=client)
                return render(request, 'page/checkout.html', locals())

        if request.POST.get('form_type') == 'checkout':
            if request.user.used_promo:
                promo_id = request.user.used_promo.id
            else:
                promo_id = None
            order = Order.objects.create(client=request.user, promo_code_id=promo_id,
                                         payment_id=int(request.POST.get('payment')),
                                         shipping_id=int(request.POST.get('shipping')))
            order.save(force_update=True)
            all_cart_items = Cart.objects.filter(client_id=request.user.id)
            for item in all_cart_items:
                ItemsInOrder.objects.create(order_id=order.id, item_id=item.item.id, number=item.number,
                                            current_price=item.item.price)
                item.item.buys = item.item.buys + 1
                item.item.save(force_update=True)
            all_cart_items.delete()
            request.user.used_promo = None
            request.user.save(force_update=True)

            if promo_id:
                print('order with promo')
                order_saved = Order.objects.get(id=order.id)
                print('order total = {}'.format(order_saved.total_price))
                promo_discount_value = order_saved.promo_code.promo_discount
                print('promo discount = {}'.format(promo_discount_value))
                total_order_price_with_discount = format_number(
                    order_saved.total_price - (order_saved.total_price * promo_discount_value / 100))
                order_saved.total_price_with_code = total_order_price_with_discount

                order_saved.save(force_update=True)

        if request.POST.get('form_type') == 'checkout_guest':
            print(request.POST)
            s_key = request.session.session_key
            guest = Guest.objects.get(session=s_key)
            if guest.used_promo:
                promo_id = guest.used_promo.id
                print('With promo')
            else:
                promo_id = None
                print('With no promo')

            if request.POST.get('with_register') == 'on':
                print('With register')



    shipping = OrderShipping.objects.all()
    payment = OrderPayment.objects.all()

    if request.user.is_authenticated:
        client = request.user
        form = UpdateForm(instance=client)
        return render(request, 'page/checkout.html', locals())
    else:
        form = UpdateForm()
        return render(request, 'page/checkout.html', locals())




def index(request):
    banners = Banner.objects.filter(is_active=True).order_by('-order')
    collections = Collection.objects.filter(show_at_homepage=True)
    main_category = Category.objects.all()
    return render(request, 'page/index.html', locals())


def category(request, cat_slug):
    try:
        cat = Category.objects.get(name_slug=cat_slug)
        cat.views += 1
        cat.save(force_update=True)
        subcats = SubCategory.objects.filter(category=cat)
    except:
        return render(request, '404.html', locals())

    return render(request, 'page/category.html', locals())


def subcategory(request, subcat_slug):
    try:
        subcat = SubCategory.objects.get(name_slug=subcat_slug)
        subcat.views += 1
        subcat.save(force_update=True)
        all_items = Item.objects.filter(subcategory_id=subcat.id).order_by('name')
    except:
        return render(request, '404.html', locals())
    data = request.GET
    print(request.GET)
    search = data.get('search')
    filter = data.get('filter')
    order = data.get('order')
    page = request.GET.get('page')
    search_qs = None
    filter_sq = None
    if search:
        items = all_items.filter(name__contains=search)

        if not items:
            items = all_items.filter(article__contains=search)
        search_qs = items

        param_search = search

    if filter == 'new':
        print('Поиск по фильтру туц')
        if search_qs:
            items = search_qs.filter(is_new=True)
            filter_sq = items
            param_filter = filter
        else:
            items = all_items.filter(is_new=True)
            filter_sq = items
            param_filter = filter

        param_filter = 'new'

    if filter and filter != 'new':
        print('Поиск по фильтру')

        if search_qs:
            items = search_qs.filter(filter__name_slug=filter)
            filter_sq = items
            param_filter = filter
        else:
            items = all_items.filter(filter__name_slug=filter)
            filter_sq = items
            param_filter = filter

    if order:
        if search_qs and filter_sq:
            items = filter_sq.order_by(order)
        elif filter_sq:
            items = filter_sq.order_by(order)
        elif search_qs:
            items = search_qs.order_by(order)
        else:
            items = all_items.order_by(order)
        param_order = order

    if not search and not order and not filter:
        items = all_items
        param_order = 'name'

    items_paginator = Paginator(items, 12)

    try:
        items = items_paginator.get_page(page)
    except PageNotAnInteger:
        items = items_paginator.page(1)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)
    return render(request, 'page/subcategory.html', locals())

