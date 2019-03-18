from django.shortcuts import render,redirect

from django.http  import HttpResponse,Http404
import datetime as dt
from . models import Location, Category, Images

# Create your views here.
def welcome(request):
    photos = Images.objects.all()
    return render (request, 'welcome.html', {'photos':photos})


def display_image(request):
    date = dt.date.today()
    return render(request, 'today.html', {"date": date})


def single_photo(request, photo_id):
    photo = Images.objects.get(id=photo_id)
    return render(request, 'single_image.html', {'photo': photo})


def all_images(request):
    photo = Images.get_images()
    return render(request, 'all_images.html', {"photo": photo})


def search_results(request):
    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_photo = Image.search_by_title(search_term)
        photos = Image.objects.filter(name=searched_photo).all()
        message = f"{search_term}"
        return render(request, 'search_image.html', {"message": message, "photos": searched_photo})
    else:
        message = 'You haven\'t searched for any photos.'
        return render(request, 'search_image.html', {"message": message})
