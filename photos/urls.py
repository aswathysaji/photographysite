from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('photos',views.photo,name='photos'),
    path('videos',views.video,name='videos'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_video',views.add_video,name='add-video'),
    path('photos_list',views.photos_list,name='photo-list'),
    path('edit_photo/<photo_id>',views.edit_photo,name='edit-photo'),
    path('videos_list',views.videos_list,name='video-list'),
    path('edit_video/<video_id>',views.edit_video,name='edit-video'),
    path('delete_photo/<photo_id>',views.delete_photo,name='delete-photo'),
    path('delete_video/<video_id>',views.delete_video,name='delete-video'),
    path('messages',views.message,name='messages')
]