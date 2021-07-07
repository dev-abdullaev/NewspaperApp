from django.contrib import admin
from .models import Articles, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Articles, ArticleAdmin)


admin.site.register(Comment)
