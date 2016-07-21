from django.contrib import admin
from boardapp import models

# Register your models here.

admin.site.register(models.Board)
admin.site.register(models.Thread)
admin.site.register(models.Post)
