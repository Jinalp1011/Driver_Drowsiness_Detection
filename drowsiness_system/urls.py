from django.contrib import admin
from django.urls import path
from .views.views import index
from .views.login import Login,logout
from .views.signup import Signup
from .views.detection import detect_drowsiness


urlpatterns = [
    path('',index),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('detection',detect_drowsiness,name='detection'),
    
]
