from django.contrib import admin
from .models import Product, ProductAdditionalField


class ProductAdditionalFieldInline(admin.TabularInline):
    """
    Admin inline for ProductAdditionalField.
    Allows managing additional fields directly from the Product admin page.
    """
    model = ProductAdditionalField
    extra = 1 # Number of blank forms displayed for adding additional fields

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Specifies the fields to be displayed on the product list page
    list_display = ('name', 'barcode', 'price', 'stock', 'created_at', 'updated_at')
    
    # Define fields that can be used for search
    search_fields = ('name', 'barcode')
    
    # Specifies the filters available in the sidebar
    list_filter = ('created_at', 'updated_at')
    
    # Define field groupings in the product detail page
    fieldsets = (
        (None, {'fields': ('name', 'barcode', 'price', 'stock')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    # Add an inline for ProductAdditionalField
    inlines = [ProductAdditionalFieldInline]
    
    # Specify read-only fields
    readonly_fields = ('created_at', 'updated_at')

@admin.register(ProductAdditionalField)
class ProductAdditionalFieldAdmin(admin.ModelAdmin):
    # Specifies the fields to display in the additional fields list page
    list_display = ('product', 'name_field', 'value_field')
    
    # Specifies fields that can be used for search
    search_f




