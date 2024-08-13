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
    slug = models.SlugField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    image = models.ImageField(upload_to='media', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    published_date = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=False)  # should define

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["published_date"]

    def comments_count(self):
        comments = Comment.objects.filter(post__pk=self.pk)
        return len(comments)

    def bookmark_count(self):
        bookmark = BookMark.objects.filter(post__pk=self.pk)
        return len(bookmark)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    email = models.EmailField()
    approved = models.BooleanField()
    created_date = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'Comment by {self.author} is {self.message}'


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
