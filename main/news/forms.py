from django import forms
from .models import Category, News
from django.core.exceptions import ValidationError

class NewsForms(forms.Form):
    title = forms.CharField(max_length=150,  label='Наименование',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Контент', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control', 'rows': 5, }))
    is_published = forms.BooleanField(label='Публикация', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      empty_label='Выберите категорию',
                                      widget=forms.Select(attrs={'class': 'form-control', }))


class NewsFormsModel(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': 5})

        #self.fields['photo'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'is_published', 'category']

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0].isdigit():
            raise ValidationError('Наименование не может начинаться с цифры!')
        return title.capitalize()

    def clean_content(self):
        content = self.cleaned_data['content']
        if content[0].isdigit():
            raise ValidationError('Поле контента не может начинаться с цифры!')
        elif len(content.split()) < 3:
            raise ValidationError("Поле контента должно содержать более 2(двух) слов!")
        return content.capitalize()
