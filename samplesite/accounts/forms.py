from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Никнейм')
    first_name = forms.CharField(max_length=30, label='Имя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            raise forms.ValidationError('Пароли не совпадают! \r\n Попытайтесь снова')
        return cd['password_2']
