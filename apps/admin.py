from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from apps.models import Product, Shop, Category, ProductImage, DeliveryPoint


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Shop)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class ProductAdmin(DraggableMPTTAdmin):
    pass


@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(DeliveryPoint)
class DeliveryPointAdmin(admin.ModelAdmin):
    list_display = ['city', 'location']
