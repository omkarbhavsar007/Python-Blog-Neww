from django.db import models

# Create your models here.
class ContactModel(models.Model):
        contact_feedback = models.CharField(max_length = 200)
        contact_name = models.CharField(max_length = 200)
        contact_email = models.ImageField(max_length = 200)
        contact_subject = models.ImageField(max_length = 200)