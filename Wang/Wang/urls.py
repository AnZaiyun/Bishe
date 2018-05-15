"""Wang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Travel_Web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('city_home',views.city_home),
    path('city_sight',views.city_sight),
    path('city_shopping',views.city_shopping),
    path('city_shop',views.city_shop),
    path('city_restandfood', views.city_restandfood),
    path('city_rest', views.city_rest),
    path('city_travel', views.city_travel),
    path('city_sight/search', views.search_sight),
    path('city_rest/search', views.search_rest),
    path('city_shop/search', views.search_shop),
    path('city_travel/search', views.search_travel),

]
