from django.conf import settings
from django.db import models

class Report(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)  # New field
    description = models.TextField()
    reasons = models.TextField(null=True)
    funding_required = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.owner.username} - {self.location}"
