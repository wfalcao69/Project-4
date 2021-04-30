from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.db.models import (
    DateField, DateTimeField, DurationField, Field, Func, IntegerField,
    TimeField, Transform, fields,
)


class User(AbstractUser):
    pass

class Post(models.Model):
    #name = models.CharField(max_length=64)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    content = models.CharField(max_length=264)
    #image = models.CharField(max_length=564)
    #bid = models.FloatField()
    time_of_creation = models.DateField(auto_now_add=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    #bid_on = models.BooleanField(default=True)

#    def __str__(self):
#        return f"Post {self.id}, created by {self.creator}; in {self.time_of_creation}:\n {self.content}".splitlines()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=64)
#    post_id = models.IntegerField()

    def __str__(self):
#        return f"{self.user} comments Post {self.post_id}:\n {self.comment}".splitlines()
        return f"{self.user} comments:\n {self.comment}".splitlines()


#class Comment(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    product = models.ForeignKey(Product, on_delete=models.CASCADE)
#    comment = models.CharField(max_length=64)
#    item_id = models.IntegerField()

#    def __str__(self):
#        return f"{self.user}, Product {self.item_id}: {self.comment}"
