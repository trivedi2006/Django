from django.urls import path
from app1.views import Home,About,Nav
urlpatterns = [
    path('',Home,name='Home'),
    path('About/',About,name='About'),
    path('Nav/',Nav,name='Nav')
]