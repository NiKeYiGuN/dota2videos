from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    playtime = models.IntegerField()
    position = models.CharField(max_length=32)


