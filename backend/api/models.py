from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lead(models.Model):
    STATUS_CHOICES = (
        ('Contacted', 'Contacted'),
        ('New Lead', 'New Lead'),
        ('Qualified', 'Qualified'),
    )
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
