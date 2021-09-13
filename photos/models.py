from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class Message(models.Model):
    name = models.CharField('Fullname',max_length=100)
    email = models.EmailField('Email')
    message = models.CharField('Message',max_length=500)

    def __str__(self):
        return self.name

class Video(models.Model):
    category = models.CharField('Category',max_length=50)
    heading = models.CharField('Video Heading',max_length=100)
    video = models.FileField('Video',upload_to='videos/')

    def __str__(self):
        return self.heading

class Photo(models.Model):
    category = models.CharField('Category',max_length=50)
    heading = models.CharField('Heading',max_length=100)
    description = models.CharField('Description',max_length=1000)
    image = models.ImageField('Image',upload_to='images/')

    def __str__(self):
        return self.heading