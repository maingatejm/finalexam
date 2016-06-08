from django.contrib import admin
from .models import Category, Shop, Review

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_at']

class ShopAdmin(admin.ModelAdmin):
	list_display = ['category', 'shop_name', 'created_at']

class ReviewAdmin(admin.ModelAdmin):
	list_display = ['shop', 'user', 'comment']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Review, ReviewAdmin)