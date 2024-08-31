from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the default User model

class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stores")
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='store_logos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True, null= True)  # Store social links in JSON format
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
