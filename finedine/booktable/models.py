from django.db import models

# Create your models here.
class booktable(models.Model):
    name = models.CharField(max_length=100, default='Your name')
    email = models.EmailField(max_length=100, default='abc@gmail.com')
    phone = models.CharField(max_length=20, default='1234567890')
    people = models.CharField(default='Number People')
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)
