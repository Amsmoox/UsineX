from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Admin'),
            ('employee', 'Employee'),
        ],
        default='employee'
    )
    
    is_active = models.BooleanField(default=True) 
    
    metadata = models.JSONField(blank=True, null=True)
    
    # Methods for role-based checks
    def is_admin(self):
        return self.role == 'admin'

    def is_employee(self):
        return self.role == 'employee'

    def __str__(self):
        return self.username
