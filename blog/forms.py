from django import forms

from .models import Post, Comment

# フォーム名をPostForm。Djangoのform認識のためにforms.ModelForm
class PostForm(forms.ModelForm):

    class Meta:
        # フォーム対象のモデル指定（importしてきて）
        model = Post
        # フォームの記入欄情報をfieldsに
        fields = ('title', 'text',)
        # 他fields: author は現在ログインしている人（自分自身）
        # 他fields: created_date は（コードにより）自動的に記事を書いた日時が設定


# commentモデル用
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
