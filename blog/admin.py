from django.contrib import admin

from blog.models import Post, Category, Comment, Like, BookMark, CommentReply


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    list_filter = ('status', 'author')
    ordering = ['published_date']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('author', 'post', 'message', 'created_date')
    list_filter = ('approved',)


class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ('author', 'reply_to', 'reply_message',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')


# Register models in admin
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(BookMark, BookmarkAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)
