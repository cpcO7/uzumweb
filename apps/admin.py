from django.contrib import admin

from apps.models import Product, Shop, Category, ProductImage


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Shop)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    pass

