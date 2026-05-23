from django.urls import path
from app1.views import page1
from app1.views import home
from app1.views import user
from app1.views import p1
urlpatterns = [
    path('B1/',home),
    path('user/',user),
    path('page1/',page1),
    path('p1/',p1)
]