from django import forms
from .models import Category


class NewsForms(forms.Form):
    title = forms.CharField(max_length=150, min_length=5,  label='Наименование', widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Контент', required=False, widget=forms.Textarea(attrs={
        'class':'form-control', 'rows': 5, }))
    is_published = forms.BooleanField(label='Публикация', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
        empty_label='Выберите категорию', widget=forms.Select(attrs={'class':'form-control',}))
