from django.urls import path
from . views import movie_list, movie_details

urlpatterns = [
    
    path('list/', movie_list, name='Movie-list'),
    path('list/<int:pk>/', movie_details, name='Movie_details'),
]
