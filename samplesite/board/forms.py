from django import forms
from .models import Board
import re


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', 'image', 'content', 'price', 'contacts', 'rubric')

    def clean_price(self):
        cd = self.cleaned_data
        if cd['price'] and cd['price'] < 0:
            raise forms.ValidationError('Значение цены не может быть отрицательным')
        return cd['price']

    def clean_contacts(self):
        cd = self.cleaned_data
        pattern = re.compile(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
        if not pattern.search(cd['contacts']):
            raise forms.ValidationError('Номер телефона введён некорректно! \n Пример ввода: +7 123 456 78 90 или 8 123 456 78 90\n. Скобки в коде (), дефисы для читабельности - по желанию')
        return cd['contacts']


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=50, label='')
