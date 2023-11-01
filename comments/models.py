from django.db import models


class Kino(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()


class Comment(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField()
    timedate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    kino = models.ForeignKey(Kino, on_delete=models.SET_NULL, null=True, blank=True)

