from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.all_images, name='allImages'),
    url('^day/$', views.display_image, name='Today'),
    url(r'^photo/(\d+)', views.single_photo, name='singlePhoto'),
    url(r'^all/$', views.all_images, name='allImages'),
    url(r'^search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)