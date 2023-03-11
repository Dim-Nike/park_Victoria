from django.contrib import admin
from .models import *

# Register your models here.

class CategoriesProductAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'categories', 'price', 'is_active', 'popular', 'product_is_day']

# class AnswerAskAdmin(admin.ModelAdmin):
#     list_display = ['answer', 'is_active']

admin.site.register(CategoriesProduct, CategoriesProductAdmin)
admin.site.register(MainImg)
admin.site.register(Articles)
admin.site.register(Product, ProductAdmin)
# admin.site.register(AnswerAsk, AnswerAskAdmin)