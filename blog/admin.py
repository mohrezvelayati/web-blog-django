from django.contrib import admin


from blog.models import Post, Category, Comment

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




# Register models in admin
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)