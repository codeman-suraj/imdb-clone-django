from django.urls import path, include
# from . views import movie_list, movie_details
from . views import (MovieListAV, MovieDetailAV,
                     StreamPlatformsAV,
                     StreamPlatformsdetailsAV,
                     ReviewList, ReviewDetails, ReviewCreate, StreamPlatformsvs)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformsvs.as_view(), basename='streamplatform')

urlpatterns = [
    
    path('watchlist/', MovieListAV.as_view(), name='watch-list'),
    path('watchlist/<int:pk>/', MovieDetailAV.as_view(), name='watch-list-detail'),
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformsAV.as_view(), name='streamplatform'),
    # path('stream/<int:pk>/', StreamPlatformsdetailsAV.as_view(), name='Movie_details'),
    
    # path('stream/review/', ReviewList.as_view(), name='ReviewList'),
    # path('stream/review/<int:pk>/', ReviewDetails.as_view(), name='ReviewDetails'),
    
    
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='ReviewList'),
    path('stream/review/<int:pk>/', ReviewDetails.as_view(), name='ReviewDetails'),
    
    
]
