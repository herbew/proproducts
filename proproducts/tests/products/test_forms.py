from django.test import TestCase, override_settings
from django.core.exceptions import ValidationError
from products.forms import (
    ProductCreateForm, ProductUpdateForm,
    ProductAdditionalFieldCreateForm, ProductAdditionalFieldUpdateForm
)
from products.models import Product, ProductAdditionalField


@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})


class ProductFormsTest(TestCase):
    def test_product_create_form_valid(self):
        # Data valid for form ProductCreateForm
        form_data = {
            'name': 'Test Product',
            'barcode': '123456789',
            'price': 100.00,
            'stock': 10
        }
        form = ProductCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_create_form_invalid(self):
        # Data not valid (name null)
        form_data = {
            'name': '',
            'barcode': '123456789',
            'price': 100.00,
            'stock': 10
        }
        form = ProductCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)  # maksure error on the field 'name'

    def test_product_update_form_valid(self):
        # Create the product
        product = Product.objects.create(
            name='Test Product',
            barcode='123456789',
            price=100.00,
            stock=10
        )
        # Data valid for form ProductUpdateForm
        form_data = {
            'name': 'Updated Product',
            'barcode': '987654321',
            'price': 200.00,
            'stock': 20
        }
        form = ProductUpdateForm(data=form_data, instance=product)
        self.assertTrue(form.is_valid())

    def test_product_update_form_invalid(self):
        # Create the product
        product = Product.objects.create(
            name='Test Product',
            barcode='123456789',
            price=100.00,
            stock=10
        )
        # Data not valid (price negative)
        form_data = {
            'name': 'Updated Product',
            'barcode': '987654321',
            'price': -100.00,  # Price can't negatif
            'stock': 20
        }
        form = ProductUpdateForm(data=form_data, instance=product)
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)  # Makesure error on the field 'price'


class ProductAdditionalFieldFormsTest(TestCase):
    def setUp(self):
        # Create the product
        self.product = Product.objects.create(
            name='Test Product',
            barcode='123456789',
            price=100.00,
            stock=10
        )

    def test_additional_field_create_form_valid(self):
        # Data valid for form ProductAdditionalFieldCreateForm
        form_data = {
            'product': self.product.id,
            'name_field': 'Color',
            'value_field': 'Red'
        }
        form = ProductAdditionalFieldCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_additional_field_create_form_invalid(self):
        # Data not valid (name_field null)
        form_data = {
            'product': self.product.id,
            'name_field': '',  # name_field can't null
            'value_field': 'Red'
        }
        form = ProductAdditionalFieldCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name_field', form.errors)  # makesure error on the field 'name_field'

    def test_additional_field_update_form_valid(self):
        # Create additional field 
        additional_field = ProductAdditionalField.objects.create(
            product=self.product,
            name_field='Color',
            value_field='Red'
        )
        # Data valid for form ProductAdditionalFieldUpdateForm
        form_data = {
            'product': self.product.id,
            'name_field': 'Size',
            'value_field': 'Large'
        }
        form = ProductAdditionalFieldUpdateForm(data=form_data, instance=additional_field)
        self.assertTrue(form.is_valid())

    def test_additional_field_update_form_invalid(self):
        # Create additional field 
        additional_field = ProductAdditionalField.objects.create(
            product=self.product,
            name_field='Color',
            value_field='Red'
        )
        # Data not valid (value_field null)
        form_data = {
            'product': self.product.id,
            'name_field': 'Size',
            'value_field': ''  # value_field can't null
        }
        form = ProductAdditionalFieldUpdateForm(data=form_data, instance=additional_field)
        self.assertFalse(form.is_valid())
        self.assertIn('value_field', form.errors)  # makesure error on the field 'value_field'
        
        
        
        
        
        
        