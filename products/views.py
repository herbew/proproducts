from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, ProductAdditionalField
from .forms import (ProductCreateForm, ProductUpdateForm, 
			ProductAdditionalFieldCreateForm, 
			ProductAdditionalFieldUpdateForm)
from users.mixins import MemberMixin, ManagerMixin

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductCreateView(MemberMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product_create.html'
    success_url = reverse_lazy('products:product_list')

class ProductUpdateView(MemberMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'products/product_update.html'
    success_url = reverse_lazy('products:product_list')

class ProductDeleteView(ManagerMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products:product_list')

# ProductAdditionalField Views
class ProductAdditionalFieldListView(ListView):
    model = ProductAdditionalField
    template_name = 'products/product_additional_field_list.html'
    context_object_name = 'additional_fields'

class ProductAdditionalFieldCreateView(MemberMixin, CreateView):
    model = ProductAdditionalField
    form_class = ProductAdditionalFieldCreateForm
    template_name = 'products/product_additional_field_create.html'
    success_url = reverse_lazy('products:product_additional_field_list')

class ProductAdditionalFieldUpdateView(MemberMixin, UpdateView):
    model = ProductAdditionalField
    form_class = ProductAdditionalFieldUpdateForm
    template_name = 'products/product_additional_field_update.html'
    success_url = reverse_lazy('products:product_additional_field_list')

class ProductAdditionalFieldDeleteView(ManagerMixin, DeleteView):
    model = ProductAdditionalField
    template_name = 'products/product_additional_field_delete.html'
    success_url = reverse_lazy('products:product_additional_field_list')
    
    
    
    
    