# library/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=20, blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    MANAGER = 'manager'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('ordinary', 'Ordinary User'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='ordinary')
    age = models.PositiveIntegerField(null=True, blank=True)
    # Add more custom fields as needed
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return self.username