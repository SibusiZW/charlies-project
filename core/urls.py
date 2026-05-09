from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signout/', views.signout, name='logout'),
    path('details/<int:pk>/', views.details_view, name='details'),
    path('myhacks/', views.my_hacks, name='my_hacks')
]