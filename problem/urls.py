# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.HomeView,name="home"),  	  
	path('easy/',views.EasyView,name="easy"),
	path('medium/',views.MediumView,name="medium"),
	path('hard/',views.HardView,name="hard"),
	path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
]
