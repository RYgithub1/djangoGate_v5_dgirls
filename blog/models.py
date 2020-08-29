from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField('名前', max_length=200)
    text = models.TextField('強み', blank=True)

    thumbnail = models.ImageField(
        'サムネイル', upload_to='thumbnails/', null=True, blank=True)
    # upload:ファイルの保存場所を指定する仕組み
    upload = models.FileField(
        '動画', upload_to='uploads/%Y/%m/%d/', null=True)

    # created_date = models.DateTimeField(default=timezone.now)
    # timezone.nowと違い、入力欄は表示されない
    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    # published_date = models.DateTimeField(blank=True, null=True)
    # 更新するたびにその日時が格納される
    updated_date = models.DateTimeField('Updated Date', auto_now=True)


    def publish(self):
        # self.published_date = timezone.now()
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        # return self.url

    # コメントモデルとの
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


# postへのcomment機能を追加実装 -> commentモデル作成
class Comment(models.Model):

    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # BooleanField ->true or false
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

