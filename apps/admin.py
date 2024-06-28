from django.contrib import admin

from apps.models import Product, Shop, Category, ProductImage


# Register your models here.

class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    min_num = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageStackedInline]


@admin.register(Shop)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    pass
