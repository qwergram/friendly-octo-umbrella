from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    password = models.CharField(max_length=32, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    post_id = models.IntegerField()

class Thread(models.Model):
    head = models.ForeignKey(Post, related_name="head_of")
    posts = models.ManyToManyField(Post, related_name="thread", null=True, blank=True)

class Board(models.Model):
    name = models.CharField(max_length=255, unique=True)
    maximum_threads = models.IntegerField(default=32)
    password = models.CharField(max_length=32)
    threads = models.ManyToManyField(Thread, related_name="board", null=True, blank=True)
