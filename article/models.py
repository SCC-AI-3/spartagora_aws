from re import T
from django.db import models
from django.forms import CharField
from user.models import User
from taggit.managers import TaggableManager
# Create your models here.

# like 모델,tag 앱 논의 필요

class Star(models.Model):
    star = models.CharField(max_length=20)

    def __str__(self):
        return self.star


class UpperCategory(models.Model):    
    upper_category = models.CharField(max_length=100)

    def __str__(self):
        return self.upper_category


class LowerCategory(models.Model):
    upper_category = models.ForeignKey(UpperCategory, on_delete=models.CASCADE)
    lower_category = models.CharField(max_length=100)
    lower_category_url = models.CharField(max_length=40, default='')
    def __str__(self):
        return self.lower_category

class Article(models.Model):
    user = models.ForeignKey(User, related_name="article_user",on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='', blank=True)
    content = models.CharField(max_length=5000000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    lower_category = models.ForeignKey(LowerCategory, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    count = models.IntegerField(default = 0)
    like = models.ManyToManyField(User, related_name="article_like", blank=True)
    nickname =models.CharField(max_length=50, default='')
    star = models.ForeignKey(Star, default='', on_delete=models.CASCADE)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.content



class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    article = models. ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
