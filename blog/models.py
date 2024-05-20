from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    published_date = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def comments_count(self):
        comments = Comment.objects.filter(post__pk=self.pk)
        return len(comments)
    
    def bookmark_count(self):
        bookmark = BookMark.objects.filter(post__pk=self.pk)
        return len(bookmark)



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=False)
    email = models.EmailField()
    approved = models.BooleanField()
    created_date = models.DateTimeField(default=datetime.now())


    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return str(self.message)



class CommentReply(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    reply_to = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply_message = models.TextField(blank=False, null=False)
    approved = models.BooleanField()
    created_date = models.DateTimeField(default=datetime.now())
    


    def __str__(self):
        return f"Reply to: {self.reply_to}"






class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



    def __str__(self):
        return str(self.post)



class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = "BookMark"