from django.test import TestCase, override_settings
from django.urls import reverse, resolve
from products.views import (
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductAdditionalFieldListView, ProductAdditionalFieldCreateView,
    ProductAdditionalFieldUpdateView, ProductAdditionalFieldDeleteView
)

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})


class ProductURLsTest(TestCase):
    def test_product_list_url(self):
        url = reverse('products:product_list')
        self.assertEqual(resolve(url).func.view_class, ProductListView)

    def test_product_create_url(self):
        url = reverse('products:product_create')
        self.assertEqual(resolve(url).func.view_class, ProductCreateView)

    def test_product_update_url(self):
        url = reverse('products:product_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProductUpdateView)

    def test_product_delete_url(self):
        url = reverse('products:product_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProductDeleteView)


class ProductAdditionalFieldURLsTest(TestCase):
    def test_additional_field_list_url(self):
        url = reverse('products:product_additional_field_list')
        self.assertEqual(resolve(url).func.view_class, ProductAdditionalFieldListView)

    def test_additional_field_create_url(self):
        url = reverse('products:product_additional_field_create')
        self.assertEqual(resolve(url).func.view_class, ProductAdditionalFieldCreateView)

    def test_additional_field_update_url(self):
        url = reverse('products:product_additional_field_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProductAdditionalFieldUpdateView)

    def test_additional_field_delete_url(self):
        url = reverse('products:product_additional_field_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProductAdditionalFieldDeleteView)
        