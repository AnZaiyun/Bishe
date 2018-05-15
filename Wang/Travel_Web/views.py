# -*- coding:utf-8 -*-
from django.shortcuts import render
from Travel_Web.models import *
from django.conf import settings
import json
# Create your views here.

def index(request):
   
    return render(request,'index.htm')

def city_home(request):
    if settings.CITYFLAG == 0:
        buff = request.GET['cityname']
        buff = str(buff).replace('旅游攻略','')
        print(buff)
        settings.CITYNAME = buff
        settings.CITYFLAG = 1
    cityname_etc=settings.CITYNAME+'旅游攻略'
    if Cityurl.objects.filter(city_name=cityname_etc):
        print("yes")
    else:
        print("no")
        return render(request,'information.html')

    cityinfo = Cityurl.objects.get(city_name=cityname_etc)
    print("this is check:", cityinfo)
    citypic = cityinfo.city_pic
    sight = Citysight.objects.filter(sight_city=settings.CITYNAME).order_by('?')[:6]

    context = {
        "cityname" : settings.CITYNAME,
        "citypic" : citypic,
        "sights" : sight,

    }
    return render(request,'city_home.html',context=context)

def city_sight(request):
    sight = Citysight.objects.filter(sight_city=settings.CITYNAME).order_by('?')[:30]

    context = {
        "cityname": settings.CITYNAME,
        "sights" : sight,
    }
    return render(request,'city_sight.html', context=context)

def city_shopping(request):
    shop = Cityshop.objects.filter(shop_city=settings.CITYNAME).order_by('?')[:9]
    gods = Citygods.objects.filter(gods_city=settings.CITYNAME).order_by('?')[:3]
    context = {
        "cityname" : settings.CITYNAME,
        "shops" : shop,
        "gods" : gods,
    }
    return render(request,'city_shopping.html', context=context)

def city_shop(request):
    shop = Cityshop.objects.filter(shop_city=settings.CITYNAME).order_by('?')[:30]
    context = {
        "cityname" : settings.CITYNAME,
        "shops" : shop
    }
    return render(request,'city_shop.html',context=context)

def city_restandfood(request):
    rest = Cityrestaurant.objects.filter(rest_city=settings.CITYNAME).order_by('?')[:9]
    food = Cityfood.objects.filter(food_city=settings.CITYNAME).order_by('?')[:9]
    context = {
        "cityname" : settings.CITYNAME,
        "rests" : rest,
        "foods" : food,
    }
    return render(request,'city_restandfood.html',context=context)

def city_rest(request):
    rest = Cityrestaurant.objects.filter(rest_city=settings.CITYNAME).order_by('?')[:30]
    context = {
        "cityname" : settings.CITYNAME,
        "rests" : rest,
    }
    return render(request,'city_rest.html',context=context)

def search_sight(request):
    sightname = request.GET['sightname']
    sight = Citysight.objects.filter(sight_name__contains=sightname,sight_city=settings.CITYNAME)[:50]
    context = {
        "cityname": settings.CITYNAME,
        "sights": sight,
    }
    return render(request,'city_sight.html',context=context)

def search_rest(request):
    restname = request.GET['restname']
    rest = Cityrestaurant.objects.filter(rest_name__contains=restname,rest_city=settings.CITYNAME)[:50]
    context = {
        "cityname": settings.CITYNAME,
        "rests": rest,
    }
    return render(request,'city_rest.html',context=context)

def search_shop(request):
    shopname = request.GET['shopname']
    shop = Cityshop.objects.filter(shop_name__contains=shopname,shop_city=settings.CITYNAME)[:50]
    context = {
        "shopname": settings.CITYNAME,
        "shops": shop,
    }
    return render(request,'city_shop.html',context=context)

def city_travel(request):
    travel = Citytravel.objects.filter(travel_city=settings.CITYNAME).order_by('?')[:30]
    context = {
        "cityname" : settings.CITYNAME,
        "travels" : travel,
    }
    return render(request,'city_travel.html',context=context)

def search_travel(request):
    trvaeldays = '天数：'+request.GET['traveldays']+' 天'
    traveltime = "时间："+str(request.GET['traveltime'])+" 月"
    travel = Citytravel.objects.filter(travel_city=settings.CITYNAME,travel_days__contains=trvaeldays,travel_time__contains=traveltime)

    context = {
        "cityname" : settings.CITYNAME,
        "travels" : travel,
    }
    return render(request, 'city_travel.html', context=context)
