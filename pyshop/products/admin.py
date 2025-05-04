from django.contrib import admin
from .models import Product,offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('description', 'discount', 'code')
    search_fields = ('description',)


admin.site.register(Product, ProductAdmin)
admin.site.register(offer, OfferAdmin)


