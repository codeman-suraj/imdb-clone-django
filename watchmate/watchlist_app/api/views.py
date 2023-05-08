from watchlist_app.models import (Watchlist, StreamPlatforms, Review)
from . serializers import (WatchlistSerializer, StreamPlatformsSerializer, ReviewSerializer)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# from rest_framework import mixins
from rest_framework import generics
# from rest_framework.decorators import api_view
from rest_framework import status



# **************************** Class-based Views using generic class-based views (Concrete View Classes)***************************

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)
        
        serializer.save(watchlist=watchlist)

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

# **************************************************************** Class-based Views using mixins ***********************************
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ReviewDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)




# **************************************************************** class based view ***********************************

class MovieListAV(APIView):
    
    def get(self, request):
        try:
            movie = Watchlist.objects.all()
        except Watchlist.DoesNotExist:
            return Response({"Error":"Watchlist doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(movie, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)
        
class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error':'movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(movie)
        return Response(serializer.data)
        
    def put(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#*************************** writing views using viewsets and routing *******************

class StreamPlatformsvs(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatforms.objects.all()
        serializer = StreamPlatformsSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = StreamPlatforms.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformsSerializer(watchlist)
        return Response(serializer.data)
    
class StreamPlatformsAV(APIView):
    
    def get(self, request):
        try:
            stremlist = StreamPlatforms.objects.all()
        except StreamPlatforms.DoesNotExist:
            return Response({"Error":"Streamplatform does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformsSerializer(stremlist, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)
        
class StreamPlatformsdetailsAV(APIView):
    
    def get(self, request, pk):
        try:
            stremlist = StreamPlatforms.objects.get(pk=pk)
        except StreamPlatforms.DoesNotExist:
            return Response({"Error":"Streamplatform does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformsSerializer(stremlist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        strealist = StreamPlatforms.objects.get(pk=pk)
        serializer = StreamPlatformsSerializer(strealist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        streamlist = StreamPlatforms.objects.get(pk=pk)
        streamlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# ******************************************************************** function based view ****************************


# @api_view(['GET', 'POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serializer = WatchlistSerializer(movie, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         serializer = WatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
    
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = WatchlistSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = WatchlistSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)