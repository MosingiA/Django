from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main, name='main'),
    path('clubs/', views.club, name='clubs'),
    path('clubs/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('template/', views.template, name='template'),
]