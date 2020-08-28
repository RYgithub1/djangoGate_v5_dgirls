"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views


# from blog.views import SignUp
from blog.views import SignUp


# メディア用
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    # サインアップ
    path('accounts/signup/', SignUp.as_view(), name='signup'),



    # ユーザー認証は別途urlをマイサイト側で追記、authのviewと繋ぐのでimportも追記
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    # ログアウト
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),


    # これで'http://127.0.0.1:8000/' に来たリクエストは blog.urls へリダイレクトする
    path('', include('blog.urls')),
]


# 開発環境のみ、Djangoアプリ側でメディアファイルを配信想定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
