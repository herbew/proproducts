from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
	
    class Meta:
        db_table = 'products_product'
        
    def __str__(self):
        return self.name
        
class ProductAdditionalField(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional_fields')
    name_field = models.CharField(max_length=50)
    value_field = models.CharField(max_length=100)
	
    class Meta:
        db_table = 'products_proaddfield'
        
    def __str__(self):
        return f"{self.name_field}: {self.value_field}"