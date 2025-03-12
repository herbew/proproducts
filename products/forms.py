from django import forms
from .models import Product, ProductAdditionalField

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'barcode', 'price', 'stock']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'barcode', 'price', 'stock']

class ProductAdditionalFieldCreateForm(forms.ModelForm):
    class Meta:
        model = ProductAdditionalField
        fields = ['product', 'name_field', 'value_field']

class ProductAdditionalFieldUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductAdditionalField
        fields = ['product', 'name_field', 'value_field']