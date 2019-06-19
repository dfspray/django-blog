from django.contrib import admin
from myblog.models import Post
from myblog.models import Category
from myblog.models import Comment

class InlineCategory(admin.TabularInline):
    model = Post.categories.through

class InlineComment(admin.TabularInline):
    model = Post.comments.through

class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    inlines = [InlineCategory, InlineComment]

class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    exclude = ('posts',)

class CommentAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)