from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    read_cnt = models.IntegerField(default=0)
    writer = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    context = models.CharField(max_length=1000, blank=True, null=True)
