from django.db import models

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=255, unique=True)
    maximum_threads = models.IntegerField(default=32)
    password = models.CharField(max_length=32)
    threads = models.ManyToManyField(Thread, related_name="board")

class Thread(models.Model):
    head = models.ForeignKey(Post)
    posts = models.ManyToManyField(Post, related_name="thread")

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    password = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    post_id = models.IntegerField()
