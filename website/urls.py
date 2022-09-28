from django.urls import path
from . import views

urlpatterns = [

    path('',views.join, name='home'),
    path('list',views.list,name='list'),
    
]