# サインアップ
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# (ユーザー)認証用デコレータをimport
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from .models import Post, Comment

from .forms import PostForm, CommentForm


# サインアップ系_c-bata
class SignUp(CreateView):
    form_class = SignupForm
    # form_class = UserCreationForm
    # template_name = "accounts/signup.html"
    template_name = "registration/signup.html"
    # success_url = reverse_lazy('top')
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        # formの情報を保存
        user = form.save()
        # 認証
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())


# POST系
def post_list(request):

    posts = Post.objects.filter(
        # published_date__lte=timezone.now()).order_by('published_date')
        updated_date__lte=timezone.now()).order_by('updated_date')

    return render(request, 'blog/post_list.html', {'posts': posts})


# urls.pyでidでなくpkを指定しているので、pkと書くしかないルール
def post_detail(request, pk):
    # post = Post.objects.get_object_or_404(id=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
# form作成時に、投稿postを作成するメソッド
# forms.pyのPostFormクラスを呼び出すために、上でimport
def post_new(request):

    # form_edit.htmlでsubmitすると、request.POSTにデータ保持
    # ifフォームを入力してsubmitしたら、変数method="POST"ゆえ、true
    # 一発目は未入力ゆえelseに流れて入力促すため 、form定義して、form持たせたままpost_edit.htmlに飛ばす
    if request.method == "POST":
        # form = PostForm(request.POST)
        # FILESも指定しないと保存できない
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # save()する前に、ユーザー名と日時を加えたいので、commit=False
            post = form.save(commit=False)
            post.author = request.user

            # 草稿機能追加->post.published_date = timezone.now()、をアウト
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # 問答無用でこっち一回目
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
# editなので、対象の番号を表す(自動採番していた)pkが必要
# また、フォームを作るときはそのポストをinstance（インスタンス）として渡すこと
def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        # 【１】フォームを保存する場合request.POST
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # 【２】フォームを編集するためただ開く
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
# ドラフトページ。published_date__isnull=True となる記事)のみ
def post_draft_list(request):
    posts = Post.objects.filter(
        # published_date__isnull=True).order_by('created_date')
        updated_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
# ドラフト版にタイムスタンプ付記して投稿完了
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # models.py/Postモデル/作成したpublishメソッドを利用
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
# 投稿内容の削除。全てのDjangoモデルは .delete() で削除可能
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    # 記事の一覧ページに行くようにします。なので redirect
    return redirect('post_list')


# コメント追加機能！
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
