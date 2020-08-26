from django.contrib import admin

# Register your models here.
from .models import Post, Comment


admin.site.register(Post)

# commentモデル追加
admin.site.register(Comment)
