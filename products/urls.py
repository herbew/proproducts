from django.urls import path
from .views import (
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductAdditionalFieldListView, ProductAdditionalFieldCreateView,
    ProductAdditionalFieldUpdateView, ProductAdditionalFieldDeleteView
)

app_name = "products"

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('additional-fields/', ProductAdditionalFieldListView.as_view(), name='product_additional_field_list'),
    path('additional-fields/create/', ProductAdditionalFieldCreateView.as_view(), name='product_additional_field_create'),
    path('additional-fields/update/<int:pk>/', ProductAdditionalFieldUpdateView.as_view(), name='product_additional_field_update'),
    path('additional-fields/delete/<int:pk>/', ProductAdditionalFieldDeleteView.as_view(), name='product_additional_field_delete'),
]