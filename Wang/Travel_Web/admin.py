from django.contrib import admin
from Travel_Web.models import *
from django.contrib import messages

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_name','shop_pic','shop_addre','shop_info','shop_score','shop_time','shop_city','shop_web')

admin.site.register(Cityshop,ShopAdmin)

admin.site.register(Cityurl)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name','food_pic','food_info','food_where','food_city','food_web')

    def save_model(self, request, obj, form, change):
        print(obj.food_name)
        # obj.shop_name = request.shop_name
        # print(obj.shop_name)
        if obj.food_name=='11':
            print('111')
            msg='填写错误'
            messages.add_message(request,messages.ERROR,msg)
            # messages.error(request,messages.ERROR,msg)
            return
        else:
            print('222')
            super(FoodAdmin, self).save_model(request, obj, form, change)

admin.site.register(Cityfood,FoodAdmin)

admin.site.register(Cityrestaurant)
admin.site.register(Citysight)
admin.site.register(Citytravel)
admin.site.register(Citygods)

admin.site.site_header = '旅游信息后台管理'
admin.site.site_title = '旅游行程规划系统'
