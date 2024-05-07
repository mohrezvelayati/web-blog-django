from django.db import models


from accounts.models import User


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
    published_date = models.DateTimeField()
    status = models.BooleanField(default=False)


  
    def __str__(self):
        return self.title




class Comment(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    approved = models.BooleanField()
    created_date = models.DateTimeField()



    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return self.author