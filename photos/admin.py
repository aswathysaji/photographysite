from django.contrib import admin
from . models import Photo, Video, Message

# Register your models here.
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Message)