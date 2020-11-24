from django.urls import path
from . import views
from .views import demo,fetch_data

urlpatterns = [
    path('ping/',demo,name='demo'),
    path('info',fetch_data,name='fetch'),
]

#<app>/<model>_<viewtype>.html