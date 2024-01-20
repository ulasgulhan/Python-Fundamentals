from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

    fields = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }

    fields = ['title', 'slug', 'description', 'price', 'image', 'category']


admin.site.register(Category, CategoryAdmin) # Decorator olarak classın tepesine yazabiliriz.
admin.site.register(Product, ProductAdmin)
