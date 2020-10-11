from django.shortcuts import render

# Create your views here.
def my_photos(request):
    return render(request,'gallery.html')
