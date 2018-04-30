# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from decimal import *
from django.contrib import admin
from . import models



admin.site.site_header = "Coretabs Online Shop Administration"
admin.site.site_title = "Coretabs Online Shop Administration"
admin.site.index_title = ""

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

	def make_price_zero(modeladmin, request, queryset):
		queryset.update(price=0)
	def discount_20(modeladmin,request,queryset):
		for product in queryset:
			discount = Decimal(product.price) * Decimal(0.2)
			queryset.update(price=product.price - discount)

	make_price_zero.short_description = "Make selected products free"
	discount_20.short_description = "Make 20%% Discount"
	date_hierarchy = 'created_at'
	search_fields = ['name']
	list_display = ('name','stock','price','description', 'category',date_hierarchy)
	list_filter = ('created_at', 'category')
	actions = [make_price_zero,discount_20]

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	date_hierarchy="created_at"
	search_field=["name"]
	list_display=("name","slug",)