from django.contrib import admin


from blog.models import Post, Category, Comment, Like, BookMark

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    list_filter = ('status', 'author')
    ordering = ['published_date']
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('author', 'post', 'created_date')
    list_filter = ('approved',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')




class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')

# Register models in admin
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(BookMark, BookmarkAdmin)