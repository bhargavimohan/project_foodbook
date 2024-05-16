from django.db import models
from django.core.validators import RegexValidator

class Recipe(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=255)
    chef_username = models.CharField(max_length=255, unique=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9_]*$',
            message='Username must be alphanumeric or contain underscores'
        ),
    ])  # A unique username for the chef
    image = models.ImageField(upload_to='recipes/')
    nutrition = models.TextField()
    health_benefits = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title
