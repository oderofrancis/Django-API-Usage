from django.db import models
import uuid
# Create your models here.

class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.uuid}"
    
    class Meta:
        verbose_name_plural = "Companies"

class Advocate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} - {self.id}"
    