from django.db import models

# Create your models here.
class Product_Category(models.Model):
    product_categotyId=models.IntegerField(primary_key=True)
    product_categotyName=models.CharField(max_length=100)
    def __str__(self):
        return self.product_categotyName
class Product(models.Model):
    product_categotyName=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    productId=models.PositiveIntegerField()
    productName=models.CharField(max_length=100)
    productPrice=models.IntegerField()
    productDate=models.DateField()

    def __str__(self):
        return self.productName
        