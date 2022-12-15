from django import forms
from .models import Category, News


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

