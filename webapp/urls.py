
"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('u_', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('u_', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('u_blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [


    path('', views.homepage, name="n_home"),
    path('a_adminhome/', views.adminhomedef, name="adminhomedef"),
    path('a_adminlogout/', views.adminlogoutdef, name="adminlogoutdef"),
    
    
    path('u_loginaction/', views.userloginaction, name="n_loginaction"),
    path('u_signup/', views.signuppage, name="n_signup"),
    
    path('u_userhome/', views.userhomedef, name="userhomedef"),
    path('u_userlogout/', views.userlogoutdef, name="userlogoutdef"),
    
    path('datasetupload/', views.datasetupload, name="datasetupload"),
    path('viewdataset/', views.viewdataset, name="viewdataset"),
    path('addfood/', views.addfood, name="addfood"),
    path('addfoodaction/', views.addfoodaction, name="addfoodaction"),
    path('diary/', views.diarydef, name="diary"),
    path('generate_bar_graph/', views.generate_bar_graph, name="generate_bar_graph"),
    path('food_rec/', views.food_rec, name="food_rec"),
    path('rda/', views.rda, name="rda"),
    path('rda2/', views.rda2, name="rda2"),
    path('viewprofilepage/', views.viewprofilepage, name="viewprofilepage"),
    path('updateprofile/', views.updateprofile, name="updateprofile"),
    


]
