from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from .forms import SignUpForm


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