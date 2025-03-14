from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model

from products.models import Product, ProductAdditionalField

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})


class ProductTemplatesTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        User = get_user_model()
        
        self.manager = User.objects.create_user(
            username='manager',
            password='managerpassword123',
            type='002'  # Manager
        )
        
        self.member = User.objects.create_user(
            username='member',
            password='memberpassword123',
            type='003'  # Member
        )
        
        self.product = Product.objects.create(
            name='Test Product',
            barcode='123456789',
            price=100.00,
            stock=10
        )
        
        self.additional_field = ProductAdditionalField.objects.create(
            product=self.product,
            name_field='Color',
            value_field='Red'
        )

    def test_product_list_template(self):
        response = self.client.get(reverse('products:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertContains(response, 'Test Product')
        self.assertContains(response, '123456789')
        self.assertContains(response, '100.00')

    def test_product_create_template(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.get(reverse('products:product_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_create.html')
        self.assertContains(response, '<form method="post">')
        self.assertContains(response, 'Create Product')

    def test_product_update_template(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.get(reverse('products:product_update', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_update.html')
        self.assertContains(response, '<form method="post">')
        self.assertContains(response, 'Update Product')

    def test_product_delete_template(self):
        self.client.login(username='manager', password='managerpassword123')
        response = self.client.get(reverse('products:product_delete', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_delete.html')
        self.assertContains(response, 'Are you sure you want to delete Test Product?')

    def test_product_additional_field_list_template(self):
        response = self.client.get(reverse('products:product_additional_field_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_additional_field_list.html')
        self.assertContains(response, 'Color')
        self.assertContains(response, 'Red')

    def test_product_additional_field_create_template(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.get(reverse('products:product_additional_field_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_additional_field_create.html')
        self.assertContains(response, '<form method="post">')
        self.assertContains(response, 'Create Additional Field')

    def test_product_additional_field_update_template(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.get(reverse('products:product_additional_field_update', args=[self.additional_field.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_additional_field_update.html')
        self.assertContains(response, '<form method="post">')
        self.assertContains(response, 'Update Additional Field')

    def test_product_additional_field_delete_template(self):
        self.client.login(username='manager', password='managerpassword123')
        response = self.client.get(reverse('products:product_additional_field_delete', args=[self.additional_field.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_additional_field_delete.html')
        #self.assertContains(response, 'Are you sure you want to delete Color: Red?')
        
        
        
        
        
        