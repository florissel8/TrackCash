from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='photos_profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True, max_length=300)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"