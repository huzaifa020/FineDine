from django.db import models

# Create your models here.
class contactform(models.Model):
    name = models.CharField(max_length=100, default='Your name')
    email = models.EmailField(max_length=100, default='abc@gmail.com')
    subject = models.CharField(max_length=100, default='Subject')
    message = models.TextField(default='Write Message...')