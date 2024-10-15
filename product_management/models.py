from django.db import models
import uuid

# Create your models here.
class Category(models.Model):
    category_unique_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_unique_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    product_name = models.CharField(max_length=50)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name