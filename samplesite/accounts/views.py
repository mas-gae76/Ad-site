from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm


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
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return render(request, 'auth/profile.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/board/')
