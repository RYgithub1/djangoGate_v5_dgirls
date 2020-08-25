from django import forms

from .models import Post


# フォーム名をPostForm。Djangoのform認識のためにforms.ModelForm
class PostForm(forms.ModelForm):

    class Meta:
        # フォームのモデル指定
        model = Post
        # フォームの記入欄情報をfieldsに
        fields = ('title', 'text',)
        # author は現在ログインしている人（自分自身）
        # created_date は（コードによって）自動的に記事を書いた日時が設定
