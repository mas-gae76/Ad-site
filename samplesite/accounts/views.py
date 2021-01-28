from django.http import HttpResponse, HttpResponseRedirect
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
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return render(request, 'auth/profile.html', {'new_user': user})
    else:
        user_form = RegisterForm()
    return render(request, 'auth/register.html', {'user_form': user_form})


def logout_view(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/board/')