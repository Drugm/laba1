from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('cinemadelux', views.about, name='cinema'),
    path('reviews', views.reviews, name='reviews'),
    path('we', views.We, name='we')
]