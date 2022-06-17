from django.urls import path  # import path
from . import views  # import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
