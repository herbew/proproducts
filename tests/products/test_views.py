from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Product, ProductAdditionalField

User = get_user_model()

class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
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

    def test_product_list_view(self):
        response = self.client.get(reverse('products:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertContains(response, 'Test Product')

    def test_product_create_view_get(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.get(reverse('products:product_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_create.html')

    def test_product_create_view_post(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.post(reverse('products:product_create'), {
            'name': 'New Product',
            'barcode': '987654321',
            'price': 200.00,
            'stock': 20
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Product.objects.filter(name='New Product').exists())

    def test_product_update_view_get(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.get(reverse('products:product_update', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_update.html')

    def test_product_update_view_post(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.post(reverse('products:product_update', args=[self.product.id]), {
            'name': 'Updated Product',
            'barcode': '987654321',
            'price': 200.00,
            'stock': 20
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')

    def test_product_delete_view_get(self):
        self.client.login(username='manager', password='managerpassword123')
        response = self.client.get(reverse('products:product_delete', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_delete.html')

    def test_product_delete_view_post(self):
        self.client.login(username='manager', password='managerpassword123')
        response = self.client.post(reverse('products:product_delete', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())


class ProductAdditionalFieldViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
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

    def test_additional_field_list_view(self):
        response = self.client.get(reverse('products:product_additional_field_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_additional_field_list.html')
        self.assertContains(response, 'Color')
        self.assertContains(response, 'Red')

    def test_additional_field_create_view_get(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.get(reverse('products:product_additional_field_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_additional_field_create.html')

    def test_additional_field_create_view_post(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.post(reverse('products:product_additional_field_create'), {
            'product': self.product.id,
            'name_field': 'Size',
            'value_field': 'Large'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(ProductAdditionalField.objects.filter(name_field='Size').exists())

    def test_additional_field_update_view_get(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.get(reverse('products:product_additional_field_update', args=[self.additional_field.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_additional_field_update.html')

    def test_additional_field_update_view_post(self):
        self.client.login(username='member', password='memberpassword123')
        response = self.client.post(reverse('products:product_additional_field_update', args=[self.additional_field.id]), {
            'product': self.product.id,
            'name_field': 'Updated Color',
            'value_field': 'Blue'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.additional_field.refresh_from_db()
        self.assertEqual(self.additional_field.name_field, 'Updated Color')

    def test_additional_field_delete_view_get(self):
        self.client.login(username='manager', password='managerpassword123')
        response = self.client.get(reverse('products:product_additional_field_delete', args=[self.additional_field.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_additional_field_delete.html')

    def test_additional_field_delete_view_post(self):
        self.client.login(username='manager', password='managerpassword123')
        response = self.client.post(reverse('products:product_additional_field_delete', args=[self.additional_field.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(ProductAdditionalField.objects.filter(id=self.additional_field.id).exists())
        
        
        
        