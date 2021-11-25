from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')


class Invitation(models.Model):
    username_invited = models.CharField(max_length=1000)
    invited_by = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=1000)


class Image(models.Model):
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
    header_image = models.FileField(null=True, blank=True, upload_to='images/')
