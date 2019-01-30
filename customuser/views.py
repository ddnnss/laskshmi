from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from .forms import SignUpForm, UpdateForm
from order.models import Wishlist,Order
from django.core.mail import send_mail
from django.template.loader import render_to_string


def account(request):
    if request.user.is_authenticated:
        return render(request, 'customuser/account.html', locals())
    else:
        return HttpResponseRedirect('/')

def orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(client=request.user)
        return render(request, 'customuser/orders.html', locals())
    else:
        return HttpResponseRedirect('/')

def order(request, order_code):
    if request.user.is_authenticated:
        order = Order.objects.get(order_code=order_code)
        return render(request, 'customuser/order.html', locals())
    else:
        return HttpResponseRedirect('/')

def account_edit(request):

    client = request.user

    if request.POST:
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            client.profile_ok = True
            client.save(force_update=True)

        return render(request, 'customuser/account_edit.html', locals())
    else:
        form = UpdateForm(instance=client)
        return render(request, 'customuser/account_edit.html', locals())


def wishlist(request):
    if request.user.is_authenticated:
        wish_list = Wishlist.objects.filter(client=request.user)

        return render(request, 'customuser/wishlist.html', locals())
    else:
        return HttpResponseRedirect('/')




def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


def log_in(request):
    return_dict = {}
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email)

    user = authenticate(email=email, password=password)
    print(user)
    if user is not None:
        if user.is_active:
            login(request, user)
            return_dict['result'] = 'success'
            return JsonResponse(return_dict)
        else:
            return_dict['result'] = 'inactive'
            return JsonResponse(return_dict)
    else:
        return_dict['result'] = 'invalid'
        return JsonResponse(return_dict)
    return_dict['result'] = 'denied'
    return JsonResponse(return_dict)


def signup(request):
    return_dict = {}
    if request.method == 'POST':
        n1 = int(request.POST.get('n1'))
        n2 = int(request.POST.get('n2'))
        answer = int(request.POST.get('answer'))
        if n1 + n2 == answer:
            print(request.POST)
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            data = {'email': email, 'password2': password2, 'password1': password1}
            form = SignUpForm(data=data)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                print('User registred')
                msg_html = render_to_string('email/register.html', {'login': email, 'password': password1})
                send_mail('Регистрация на сайте LAKSHMI888', None, 'info@lakshmi888.ru', [email],
                          fail_silently=False, html_message=msg_html)
                print('Email sent to {} with pass {}'.format(email,password1))
                login(request, user)


                return_dict['result'] = 'success'
                return JsonResponse(return_dict)
            else:
                return_dict['result'] = form.errors
                print(return_dict)
                return JsonResponse(return_dict)
        else:
            return_dict['result'] = 'bad'
            return JsonResponse(return_dict)

    else:
            form = SignUpForm()
    return_dict['result'] = 'not post'
    return JsonResponse(return_dict)