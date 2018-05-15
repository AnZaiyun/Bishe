# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cityfood(models.Model):


    food_name = models.CharField(primary_key=True, max_length=255, verbose_name='食物名字')
    food_pic = models.CharField(max_length=255, blank=True, null=True, verbose_name='食物图片')
    food_info = models.CharField(max_length=2000, blank=True, null=True, verbose_name='食物介绍')
    food_where = models.CharField(max_length=2000, blank=True, null=True, verbose_name='购买地点')
    food_city = models.CharField( max_length=255, blank=True, null=True, verbose_name='所在城市')
    food_web = models.CharField(max_length=255, blank=True, null=True, verbose_name='来源网站')

    class Meta:
        managed = False
        db_table = 'cityfood'
        verbose_name = '特色美食信息'
        verbose_name_plural = '特色美食信息'


class Citygods(models.Model):
    gods_name = models.CharField(primary_key=True, max_length=255)
    gods_pic = models.CharField(max_length=255, blank=True, null=True)
    gods_info = models.CharField(max_length=2550, blank=True, null=True)
    gods_where = models.CharField(max_length=255, blank=True, null=True)
    gods_city = models.CharField(max_length=255, blank=True, null=True)
    gods_web = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citygods'
        verbose_name = '特色商品信息'
        verbose_name_plural = '特色商品信息'


class Cityrestaurant(models.Model):
    rest_name = models.CharField(primary_key=True, max_length=255)
    rest_city = models.CharField(max_length=255, blank=True, null=True)
    rest_pic = models.CharField(max_length=255, blank=True, null=True)
    rest_info = models.CharField(max_length=255, blank=True, null=True)
    rest_food = models.CharField(max_length=255, blank=True, null=True)
    rest_addre = models.CharField(max_length=255, blank=True, null=True)
    rest_tel = models.CharField(max_length=255, blank=True, null=True)
    rest_time = models.CharField(max_length=255, blank=True, null=True)
    rest_price = models.CharField(max_length=255, blank=True, null=True)
    rest_score = models.CharField(max_length=255, blank=True, null=True)
    rest_web = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cityrestaurant'
        verbose_name = '餐馆信息'
        verbose_name_plural = '餐馆信息'


class Cityshop(models.Model):
    shop_name = models.CharField(primary_key=True, max_length=255, verbose_name='商店名称')
    shop_pic = models.CharField(max_length=255, blank=True, null=True, verbose_name='商店图片')
    shop_addre = models.CharField(max_length=255, blank=True, null=True, verbose_name='商店地址')
    shop_info = models.CharField(max_length=2000, blank=True, null=True, verbose_name='商店信息')
    shop_score = models.CharField(max_length=255, blank=True, null=True, verbose_name='商店评分')
    shop_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='营业时间')
    shop_city = models.CharField(max_length=255, blank=True, null=True, verbose_name='所在城市')
    shop_web = models.CharField(max_length=255, blank=True, null=True, verbose_name='来源网站')

    class Meta:
        managed = False
        db_table = 'cityshop'
        verbose_name = '商店信息'
        verbose_name_plural = '商店信息'


class Citysight(models.Model):
    sight_name = models.CharField(primary_key=True, max_length=255)
    sight_city = models.CharField(max_length=255, blank=True, null=True)
    sight_pic = models.CharField(max_length=1000, blank=True, null=True)
    sight_info = models.CharField(max_length=2550, blank=True, null=True)
    sight_score = models.CharField(max_length=255, blank=True, null=True)
    sight_addre = models.CharField(max_length=500, blank=True, null=True)
    sight_time = models.CharField(max_length=255, blank=True, null=True)
    sight_web = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citysight'
        verbose_name = '景点信息'
        verbose_name_plural = '景点信息'


class Citytravel(models.Model):
    travel_name = models.CharField(primary_key=True, max_length=255)
    travel_days = models.CharField(max_length=255, blank=True, null=True)
    travel_price = models.CharField(max_length=255, blank=True, null=True)
    travel_time = models.CharField(max_length=255, blank=True, null=True)
    travel_places = models.CharField(max_length=255, blank=True, null=True)
    travel_info = models.CharField(max_length=20000, blank=True, null=True)
    travel_city = models.CharField(max_length=255, blank=True, null=True)
    travel_pic = models.CharField(max_length=255, blank=True, null=True)
    travel_web = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citytravel'
        verbose_name = '行程信息'
        verbose_name_plural = '行程信息'


class Cityurl(models.Model):
    city_name = models.CharField(primary_key=True, max_length=255)
    city_pic = models.CharField(max_length=255, blank=True, null=True)
    city_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cityurl'
        verbose_name = '城市网址'
        verbose_name_plural = '城市网址'

