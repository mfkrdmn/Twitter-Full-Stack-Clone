from django import views
from django.urls import path
from . import views

urlpatterns = [

    path('profile/', views.profile, name='profile'),
   # path('/<str:pk>/', views.profile, name='profile'),

]



