# サインアップ
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from django import forms

# from .models import Post, Comment, Video
from .models import Post, Comment


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


# フォーム名をPostForm。Djangoのform認識のためにforms.ModelForm
class PostForm(forms.ModelForm):

    class Meta:
        # フォーム対象のモデル指定（importしてきて）
        model = Post
        # フォームの記入欄情報をfieldsに＿＿(原版２変数)
        # fields = ('title', 'text',)
        # 他fields: author は現在ログインしている人（自分自身）
        # 他fields: created_date は（コードにより）自動的に記事を書いた日時が設定
        fields = ('title', 'text', 'thumbnail', 'upload',)
        widgets = {
            # <input type="text" class="form-control"
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            # <textarea class="form-cotrol"
            # 'description': forms.Textarea(attrs={
            #     'class': 'form-control',
            # }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
            }),

            # <input type="file" class="form-control-file"
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
                # bootstrap4は下
                # 'class': "form-control",
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
                # bootstrap4は下
                # 'class': "form-control",
            }),
        }


# commentモデル用
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


# メディア用（プロフィールへ統合して削除）
# class VideoCreateForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         # fields = ('title', 'description', 'thumbnail', 'upload')
#         fields = ('title', 'text', 'thumbnail', 'upload')

#         widgets = {
#             # <input type="text" class="form-control"
#             'title': forms.TextInput(attrs={
#                 'class': 'form-control',
#             }),
#             # <textarea class="form-cotrol"
#             # 'description': forms.Textarea(attrs={
#             #     'class': 'form-control',
#             # }),
#             'text': forms.Textarea(attrs={
#                 'class': 'form-control',
#             }),

#             # <input type="file" class="form-control-file"
#             'thumbnail': forms.ClearableFileInput(attrs={
#                 'class': "form-control-file",
#                 # bootstrap4は下
#                 # 'class': "form-control",
#             }),
#             'upload': forms.ClearableFileInput(attrs={
#                 'class': "form-control-file",
#                 # bootstrap4は下
#                 # 'class': "form-control",
#             }),
#         }
