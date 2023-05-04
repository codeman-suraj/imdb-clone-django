from django.urls import path
# from . views import movie_list, movie_details
from . views import MovieListAV, MovieDetailAV, StreamPlatformsAV, StreamPlatformsdetailsAV

urlpatterns = [
    
    path('watchlist/', MovieListAV.as_view(), name='watch-list'),
    path('watchlist/<int:pk>/', MovieDetailAV.as_view(), name='watch-list-detail'),
    path('streamplatform/', StreamPlatformsAV.as_view(), name='streamplatform'),
    path('streamplatform/<int:pk>/', StreamPlatformsdetailsAV.as_view(), name='Movie_details'),
]
