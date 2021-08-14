
from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.myMainPage,name='myMainPage'),
    path('', views.myMainPage,name='myMainPage'),
   
   ]
