from django.urls import path
from webpage.views import webpage
from webpage.views import search


urlpatterns = [
    path('webpage/', webpage),
    path('webpage/', search),
]