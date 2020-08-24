from django.urls import path
from . import views


urlpatterns = [
    # name='post_list' は、ビューを識別するために使われるURL の名前
    # つまり、ビューで、def post_list():にして識別するってこと
    path('', views.post_list, name='post_list'),
    path('post/<int:pk/>', views.post_detail, name='post_detail'),
]
