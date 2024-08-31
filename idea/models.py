from django.conf import settings
from django.db import models

class Idea(models.Model):
    CATEGORY_CHOICES = [
        ('TECH', 'Technology'),
        ('FIN', 'Finance'),
        ('EDU', 'Education'),
        ('HEALTH', 'Healthcare'),
        ('AGR', 'Agriculture'),
    ]
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ideas")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255, blank=True, null=True)
    expenses = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
