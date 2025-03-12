from django.test import TestCase, override_settings
from products.models import Product, ProductAdditionalField

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(
            name='Test Product',
            barcode='123456789',
            price=100.00,
            stock=10
        )
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.barcode, '123456789')
        self.assertEqual(product.price, 100.00)
        self.assertEqual(product.stock, 10)

class ProductAdditionalFieldModelTest(TestCase):
    def test_create_additional_field(self):
        product = Product.objects.create(
            name='Test Product',
            barcode='123456789',
            price=100.00,
            stock=10
        )
        additional_field = ProductAdditionalField.objects.create(
            product=product,
            name_field='Color',
            value_field='Red'
        )
        self.assertEqual(additional_field.name_field, 'Color')
        self.assertEqual(additional_field.value_field, 'Red')