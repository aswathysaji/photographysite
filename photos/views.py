from django.shortcuts import render, redirect
from .models import Message, Photo, Video
from django.core.mail import send_mail
import os

# Create your views here.
def message(request):
    messages = Message.objects.all()
    return render(request,'messages.html',{
        "messages" : messages
    })

def delete_video(request,video_id):
    video = Video.objects.get(pk=video_id)
    video.delete()
    return redirect('video-list')

def delete_photo(request,photo_id):
    photo = Photo.objects.get(pk=photo_id)
    photo.delete()
    return redirect('photo-list')

def edit_video(request,video_id):
    video = Video.objects.get(pk=video_id)
    if request.method == 'POST':
        video.category = request.POST['category']
        video.heading = request.POST['heading']
        if len(request.FILES) != 0:
            if len(video.video) > 0:
                os.remove(video.video.path)
            video.video = request.FILES['video']
        video.save()
        return redirect('video-list')
    return render(request,'editvideo.html',{
        "video" : video
    })

def videos_list(request):
    videos = Video.objects.all()
    return render(request,'videolist.html',{
        "videos" : videos
    })

def edit_photo(request,photo_id):
    photo = Photo.objects.get(pk=photo_id)
    if request.method == 'POST':
        photo.category = request.POST['category']
        photo.heading = request.POST['heading']
        photo.description = request.POST['description']
        if len(request.FILES) != 0:
            if len(photo.image) > 0:
                os.remove(photo.image.path)
            photo.image = request.FILES['image']
        photo.save()
        return redirect('photo-list')
    return render(request,'editphoto.html',{
        "photo" : photo
    })

def photos_list(request):
    photos = Photo.objects.all()
    return render(request,'photolist.html',{
        "photos" : photos
    })

def add_video(request):
    if request.method == "POST":
        category = request.POST['category']
        heading = request.POST['heading']
        if len(request.FILES)!=0:
            video = request.FILES['video']
        videos = Video(category=category,heading=heading,video=video)
        videos.save()
        return redirect('add-video')
    else:
        return render(request,'addvideo.html',{})

def dashboard(request):
    if request.method == "POST":
        category = request.POST['category']
        heading = request.POST['heading']
        description = request.POST['description']
        if len(request.FILES)!=0:
            image = request.FILES['image']
        photo = Photo(category=category,heading=heading,description=description,image=image)
        photo.save()
        return redirect('dashboard')
    else:
        return render(request,'dashboard.html',{})

def video(request):
    videos = Video.objects.all()
    return render(request,'videos.html',{
        "videos" : videos
    })
    
def photo(request):
    photos = Photo.objects.all()
    return render(request,'photos.html',{
        "photos" : photos
    })

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        messages = request.POST['message']
        message = Message(name=name,email=email,message=messages)
        message.save()
        return redirect('contact')
    else:
        return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def home(request):
    photos = Photo.objects.all()
    return render(request,'home.html',{
        "photos" : photos
    })