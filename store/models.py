from django.conf import settings
from django.db import models

class Store(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='store_logos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True, null=True)  
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
