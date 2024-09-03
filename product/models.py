from django.db import models
from store.models import Store  # Make sure you have the Store model in store app
# from django.contrib.contenttypes.fields import GenericRelation
# from .models import Like
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    # likes = GenericRelation(Like)
    def __str__(self):
        return self.name
