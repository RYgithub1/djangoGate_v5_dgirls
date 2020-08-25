from django.shortcuts import render, get_object_or_404

from django.utils import timezone
from .models import Post

from .forms import PostForm


def post_list(request):

    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})


# urls.pyでidでなくpkを指定しているので、pkと書くしかないルール
def post_detail(request, pk):
    # post = Post.objects.get_object_or_404(id=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# form作成時に、投稿postを作成するメソ
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
