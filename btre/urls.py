from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),  # connect pages urls to projects urls
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls)
]
