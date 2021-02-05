from django import forms
from .models import Board


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', 'content', 'price', 'rubric')


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=50, label='')
