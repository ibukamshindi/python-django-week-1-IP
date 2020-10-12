from django.shortcuts import render
from .models import Photos

# Create your views here.
def my_photos(request):
    photos = Photos.objects.all()
    return render(request,'gallery.html', {"photos":photos})

def single_photo(request, photo_id):
    photo = Photos.objects.get(id=photo_id)
    return render(request, 'photo.html', {'photo':photo})
