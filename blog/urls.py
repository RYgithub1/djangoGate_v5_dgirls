from django.urls import path
from . import views


urlpatterns = [
    # name='post_list' は、ビューを識別するために使われるURL の名前
    # つまり、ビューで、def post_list():にして識別するってこと
    path('', views.post_list, name='post_list'),
    # url最後の/がないと,正確でないのでエラー発生。ブラウザ検索の自動補完はない様子
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('post/new/', views.post_new, name='post_new'),
]
