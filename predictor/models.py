from django.db import models
from django.contrib.auth.models import User

class Xray(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    result = models.CharField(max_length=20, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
