from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('sale/', views.sale, name='sale'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('property/<detid>', views.property, name='property'),
    path('contact/', views.contact, name='contact'),
    path('savecontact/', views.savecontact, name='savecontact'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
