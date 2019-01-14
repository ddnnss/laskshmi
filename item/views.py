from django.shortcuts import render
from django.http import JsonResponse
from item.models import Item,ItemImage
from cart.models import Cart
from customuser.models import User, Guest

def quick_view(request):
    return_dict = {}
    data = request.POST
    item_id = int(data.get('item_id'))
    item = Item.objects.get(id=item_id)
    images = ItemImage.objects.filter(item_id=item_id)
    if item.discount > 0:
        return_dict['item_price_discount'] = item.discount_value
    return_dict['item_id'] = item.id
    return_dict['item_name'] = item.name
    return_dict['item_name_slug'] = item.name_slug
    return_dict['item_description'] = item.description
    return_dict['item_price'] = item.price
    return_dict['item_discount'] = item.discount
    return_dict['item_new'] = item.is_new
    return_dict['item_article'] = item.article
    return_dict['item_images'] = list()
    for image in images:
        return_dict['item_images'].append(image.image_small)
    return JsonResponse(return_dict)


def add_to_cart(request):
    return_dict = {}
    try:
        request.session['user']
        print('user')
    except KeyError:
        s_key = request.session.session_key
        request.session['user'] = 'guest'
        print('guest')
        if not s_key:
            request.session.cycle_key()

    print(s_key)
    user = request.user
    print(user)

    data = request.POST
    item_id = int(data.get('item_id'))
    item_number = int(data.get('item_number'))
    if request.user.is_authenticated:
        print('User is_authenticated')
        all_items_in_cart = Cart.objects.filter(client=request.user)
    else:
        print('User is_not authenticated')
        try:
            guest = Guest.objects.get(session=s_key)
            print('Guest already created')
        except:
            guest = None

        if not guest:
            guest = Guest.objects.create(session=s_key, email='null@null.null')
            guest.save()
            print('Guest created')

        addtocart, created = Cart.objects.get_or_create(guest=guest,
                                                           item_id=item_id, defaults={'number': item_number})
        if not created:
            addtocart.number += int(item_number)
            addtocart.save(force_update=True)

        all_items_in_cart = Cart.objects.filter(guest=guest)
    count_items_in_cart = all_items_in_cart.count()
    total_cart_price = 0

    return_dict['total_items_in_cart'] = count_items_in_cart
    return_dict['all_items'] = list()
    for item in all_items_in_cart:
        total_cart_price += item.total_price
        item_dict = dict()
        item_dict['id'] = item.item.id
        item_dict['name'] = item.item.name
        item_dict['subcategory'] = item.item.subcategory.name
        item_dict['price'] = item.current_price
        item_dict['total_price'] = item.total_price
        item_dict['number'] = item.number
        item_dict['image'] = str(item.item.image)
        return_dict['all_items'].append(item_dict)

    return_dict['total_cart_price'] = total_cart_price

    return JsonResponse(return_dict)

