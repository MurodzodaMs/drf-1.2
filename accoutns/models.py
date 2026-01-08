from django.db import models
from task.models import CustomUser

class UserProfile(models.Model):
    bio = models.TextField(blank=True, null=True)
    fullname = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    user = models.OneToOneField(CustomUser, related_name='owner', on_delete=models.CASCADE)


