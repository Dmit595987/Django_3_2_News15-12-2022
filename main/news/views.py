from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForms, NewsFormsModel


def index(request):
    cont = {
        'news': News.objects.all(),
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context=cont)


def get_category(request, category_id):
    cont = {
        'news': News.objects.filter(category_id=category_id),
        'category': Category.objects.get(pk=category_id),
        'title': 'Статьи по категориям',
        }
    return render(request, 'news/category.html', context=cont)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForms(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            new = News.objects.create(**form.cleaned_data)
            return redirect(new)
    else:
        form = NewsForms()
    return render(request, 'news/add_news.html', {'form': form})


def add_news_1(request):
    if request.method == 'POST':
        form = NewsFormsModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewsFormsModel()
    return render(request, 'news/add_news_1.html', {'form': form})