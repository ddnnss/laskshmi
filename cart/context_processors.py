from .models import Cart, Guest


def items_in_cart(request):
    if request.user.is_authenticated:
        all_items_in_cart = Cart.objects.filter(client_id=request.user.id)
        print('Cart items for auth user')
        print(all_items_in_cart)
        count_items_in_cart = all_items_in_cart.count()
        total_cart_price = 0
        for item in all_items_in_cart:
            total_cart_price += item.total_price
        print(total_cart_price)
    else:
        s_key = request.session.session_key
        try:
            guest = Guest.objects.get(session=s_key)
        except:
            guest = None
        if guest:
            all_items_in_cart = Cart.objects.filter(guest=guest)
            print('Cart items for NOT auth user')
            print(guest)

            print(all_items_in_cart)
            count_items_in_cart = all_items_in_cart.count()
            total_cart_price = 0
            for item in all_items_in_cart:
                total_cart_price += item.total_price
            print(total_cart_price)

    return locals()