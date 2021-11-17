from django.contrib import admin
from .models import Category, SubCategory, Site
# Register your models here.

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'parent')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_show', 'category')
