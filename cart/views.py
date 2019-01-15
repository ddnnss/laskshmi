from django.shortcuts import render
from django.http import JsonResponse
from cart.models import Cart
from customuser.models import Guest

def show_cart(request):


    return render(request, 'cart/cart.html', locals())


def update_cart(request):
    return_dict = {}

    data = request.POST
    print(data)
    item_id = int(data.get('item_id'))
    item_number = int(data.get('item_number'))

    item = Cart.objects.get(id=item_id)
    item.number = item_number
    item.save(force_update=True)

    s_key = request.session.session_key
    item_id = int(data.get('item_id'))

    if request.user.is_authenticated:
        print('User is_authenticated')
        all_items_in_cart = Cart.objects.filter(client=request.user)

    else:
        print('User is_not authenticated')

        guest = Guest.objects.get(session=s_key)
        all_items_in_cart = Cart.objects.filter(guest=guest)

    count_items_in_cart = all_items_in_cart.count()
    total_cart_price = 0

    return_dict['total_items_in_cart'] = count_items_in_cart
    return_dict['all_items'] = list()
    for item in all_items_in_cart:
        total_cart_price += item.total_price
        item_dict = dict()
        item_dict['id'] = item.id
        item_dict['name'] = item.item.name
        item_dict['subcategory'] = item.item.subcategory.name
        item_dict['subcategory_slug'] = item.item.subcategory.name_slug
        item_dict['name_slug'] = item.item.name_slug
        item_dict['price'] = item.current_price
        item_dict['total_price'] = item.total_price
        item_dict['number'] = item.number
        item_dict['discount'] = item.item.discount

        item_dict['image'] = item.item.itemimage_set.first().image_small
        return_dict['all_items'].append(item_dict)

    return_dict['total_cart_price'] = total_cart_price

    return JsonResponse(return_dict)

