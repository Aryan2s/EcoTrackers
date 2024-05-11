from django.contrib.auth.models import User
from django.db import models

class FormData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    def __str__(self):
        return f"Data for {self.user.username}"