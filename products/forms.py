from django import forms
from django.core.exceptions import ValidationError
from .models import Product, ProductAdditionalField

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'barcode', 'price', 'stock']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Price must be a positive number.")
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise ValidationError("Stock must be a positive number.")
        return stock

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'barcode', 'price', 'stock']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Price must be a positive number.")
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise ValidationError("Stock must be a positive number.")
        return stock

class ProductAdditionalFieldCreateForm(forms.ModelForm):
    class Meta:
        model = ProductAdditionalField
        fields = ['product', 'name_field', 'value_field']

class ProductAdditionalFieldUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductAdditionalField
        fields = ['product', 'name_field', 'value_field']