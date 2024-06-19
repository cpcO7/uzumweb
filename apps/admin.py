from django.contrib import admin

from apps.models import Category


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'parent')

