from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
    
    # def change_password(self, new_password):
    #     self.user.set_password(new_password)
    #     self.user.save()


class Course(models.Model):
    STATUS_CHOICES = (
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    )

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    additional_info = models.CharField(max_length=10000)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

