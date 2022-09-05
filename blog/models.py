
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length = 100)
    body_content = models.TextField()
    description = models.TextField(default = "Open the post to read more about!", max_length = 600)
    category_id = models.ForeignKey('Category',on_delete=models.CASCADE)
    publi = models.BooleanField(default = False)
    date_create = models.DateField(auto_now_add = True)
    author = models.CharField(max_length = 100)

    
class Category(models.Model):
    tech = models.CharField(max_length = 50)
    usecase = models.CharField(max_length = 100)
    description = models.TextField(default = "")
