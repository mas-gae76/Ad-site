from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.urls import path


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'auth/profile.html', {'form': form})
                else:
                    return HttpResponse('Из этой учётной записи уже вышли')
            else:
                return HttpResponse('Вы ввели некорректный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'auth/profile.html', {'new_user': new_user})
    else:
        user_form = RegisterForm()
    return render(request, 'auth/register.html', {'user_form': user_form})
