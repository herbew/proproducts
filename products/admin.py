from django.contrib import admin
from .models import Product, ProductAdditionalField

class ProductAdditionalFieldInline(admin.TabularInline):
	"""
	Inline admin for ProductAdditionalField.
	Allows management of additional fields directly from the Product admin page.
	"""
	model = ProductAdditionalField
	extra = 1 # Number of empty forms to display for adding additional fields

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	# Defines fields to display on the product list page
	list_display = ('name', 'barcode', 'price', 'stock', 'created_at', 'updated_at')
	
	# Defines fields that can be used for searching
	search_fields = ('name', 'barcode')
	
	# Defines filters available in the sidebar
	list_filter = ('created_at', 'updated_at')
	
	# Defines grouping of fields on the product detail page
	fieldsets = (
	(None, {'fields': ('name', 'barcode', 'price', 'stock')}),
	('Timestamps', {'fields': ('created_at', 'updated_at')}),
	)
	
	# Add inline for ProductAdditionalField
	inlines = [ProductAdditionalFieldInline]
	
	# Define fields that are read-only
	readonly_fields = ('created_at', 'updated_at')

@admin.register(ProductAdditionalField)
class ProductAdditionalFieldAdmin(admin.ModelAdmin):
	# Define fields that will be displayed on the additional fields list page
	list_display = ('product', 'name_field', 'value_field')
	
	# Define fields that can be used for searching
	search_fields = ('product__name', 'name_field', 'value_field')
	
	# Define available filters in the sidebar
	list_filter = ('product',)
	
	# Defines field grouping on the additional fields detail page
	fieldsets = (
	(None, {'fields': ('product', 'name_field', 'value_field')}),
	)
    



