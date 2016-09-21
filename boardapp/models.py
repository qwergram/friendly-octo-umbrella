from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    password = models.CharField(max_length=32, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey('Thread', related_name='posts')

    def __str__(self):
        return self.title

class Thread(models.Model):
    board = models.ForeignKey('Board', related_name='threads')

    def __str__(self):
        try:
            return Post.objects.get(thread=self.pk).title
        except Post.DoesNotExist:
            return '[untitled]'

    @property
    def head_id(self):
        return Post.objects.get(thread=self.pk).pk

class Board(models.Model):
    name = models.CharField(max_length=255, unique=True)
    shortcut = models.CharField(max_length=3, unique=True)
    maximum_threads = models.IntegerField(default=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name
