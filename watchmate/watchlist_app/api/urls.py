from django.urls import path
# from . views import movie_list, movie_details
from . views import (MovieListAV, MovieDetailAV,
                     StreamPlatformsAV,
                     StreamPlatformsdetailsAV,
                     ReviewList, ReviewDetails)

urlpatterns = [
    
    path('watchlist/', MovieListAV.as_view(), name='watch-list'),
    path('watchlist/<int:pk>/', MovieDetailAV.as_view(), name='watch-list-detail'),
    
    path('stream/', StreamPlatformsAV.as_view(), name='streamplatform'),
    path('stream/<int:pk>/', StreamPlatformsdetailsAV.as_view(), name='Movie_details'),
    
    # path('stream/review/', ReviewList.as_view(), name='ReviewList'),
    # path('stream/review/<int:pk>/', ReviewDetails.as_view(), name='ReviewDetails'),
    
    
    path('stream/<int:pk>/review-create/', ReviewList.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='ReviewList'),
    path('stream/review/<int:pk>/', ReviewDetails.as_view(), name='ReviewDetails'),
    
    
]
