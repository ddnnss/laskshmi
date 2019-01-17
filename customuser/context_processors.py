from item.models import Category
def check_profile(request):
    all_cat = Category.objects.all()
    if request.user.is_authenticated:
        print('user')

    else:
        s_key = request.session.session_key
        print('guest')
        if not s_key:
            request.session.cycle_key()



    print(request.session.session_key)



    return locals()

