from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexNews.as_view(), name='index'),
    #path('index', IndexNews.as_view(), name='index_news'),
    #path('category/<int:category_id>/', get_category,  name='get_category'),
    path('category/<int:category_id>/', CategoryNews.as_view(),  name='get_category'),
    path('news/<int:news_id>/', NewsDetail.as_view(), name='view_news'),
    path('news/add-news/', add_news, name='add_news'),
    path('news/add_news_1/', add_news_1, name='add_news_1'),
    path('news/add_news_2/', CreateNews.as_view(), name='add_news_2'),
]

