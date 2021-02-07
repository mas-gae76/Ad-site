from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile')
                else:
                    return HttpResponse('Из этой учётной записи уже вышли')
            else:
                return HttpResponse('Вы ввели некорректный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return render(request, 'registration/profile.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('index')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль был успешно обновлён!\r\n Войдите с новым паролем')
            auth.logout(request)
            return redirect('login')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку ниже')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


@csrf_exempt
def show_person_cabinet(request):
    return render(request, 'registration/profile.html')


def password_reset(request):
    if request.method == 'POST':
        reset_form = PasswordResetForm(request.POST)
        if reset_form.is_valid():
            data = reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Password Reset Requested'
                    email_template_name = 'registration/password_reset_email.html'
                    c = {
                        'email': user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email])
                    except BadHeaderError:
                        return HttpResponse('Некорректная тема письма')
                    return redirect('password_reset_done')
    reset_form = PasswordResetForm()
    return render(request=request, template_name='registration/password_reset.html', context={'password_reset_form': reset_form})


def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')


def del_user(request):
    user = User.objects.get(username=request.user)
    user.delete()
    return redirect('index')
