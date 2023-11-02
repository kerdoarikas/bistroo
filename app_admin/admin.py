from django.contrib import admin
from .models import Category, Food, Menu, MenuCategory, MenuFood

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(MenuFood)
