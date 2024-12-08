from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    form = UserLoginForm()
    if request.method =='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{user} вы вошли в аккаунт')

                if request.POST.get('next', None):   # Отправка на выбранную страницу после авторизации
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
        # else:
        #     form = UserLoginForm()
    context = {
        'title': 'LOGIN',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)

def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username} вы успешно зарегистрировались и вошли в аккаунт')
            return HttpResponseRedirect(reverse('main:index'))
        # else:
        #     form = UserRegistrationForm()

    context = {
        'title': 'Registration',
        'form': form,
    }
    return render(request, 'users/registration.html', context=context)

@login_required()
def profile(request):
    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'Данные успешно обновлены')
            return HttpResponseRedirect(reverse('user:profile'))
        # else:
        #     form = ProfileForm(instance=request.user)

    context = {
        'title': 'profile',
        'form':form,
    }
    return render(request, 'users/profile.html', context=context)

def user_cart(request):
    return render(request, 'users/user-cart.html')

@login_required()
def logout(request):
    messages.success(request, f'{request.user.username} Вы вышли из аккаунта')
    auth.logout(request)
    return redirect(reverse('main:index'))