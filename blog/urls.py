from django.urls import path
from . import views


urlpatterns = [
    # name='post_list' は、ビューを識別するために使われるURL の名前
    # つまり、ビューで、def post_list():にして識別するってこと
    path('', views.post_list, name='post_list'),

    # url最後の/がないと,正確でないのでエラー発生。ブラウザ検索の自動補完はない様子
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # フォームの作成、投稿、保存
    path('post/new/', views.post_new, name='post_new'),

    # フォームの編集
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # フォームの下書きドラフト草稿
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # フォーム内容の発行日時now()をモデルメソッドから実行して、ドラフト版の投稿完了
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),

    # 内容の削除
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),

    # Commentモデル向けルーティング
    path('post/<int:pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),

    # コメントの承認、削除のルーティング
    path('comment/<int:pk>/approve/',
         views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
