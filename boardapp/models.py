from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    password = models.CharField(max_length=32, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    post_id = models.IntegerField()
    thread = models.ForeignKey('Thread', related_name='posts')

    def __str__(self):
        return self.title

class Thread(models.Model):
    board = models.ForeignKey('Board', related_name='threads')

    def __str__(self):
        try:
            return self.head.title
        except AttributeError:
            return "[Untitled]"

class Board(models.Model):
    name = models.CharField(max_length=255, unique=True)
    shortcut = models.CharField(max_length=3, unique=True)
    maximum_threads = models.IntegerField(default=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name
