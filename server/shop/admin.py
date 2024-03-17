from django.contrib import admin
from shop.models import *

@admin.register(Profile)
class ProfileAdminAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','inventory','price','category','sub_category','likes']
    list_editable = ['price','likes','inventory']
    list_filter = ['category','sub_category']
    list_per_page = 20
    search_fields = ['name']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):   
    list_display = ['user','product_id']
    list_filter = ['product_id']
    search_fields = ['user','message']

