from django.contrib import admin
from . models import Watchlist, StreamPlatforms, Review
# Register your models here.
admin.site.register(Watchlist)
admin.site.register(StreamPlatforms)
admin.site.register(Review)
