from django.db import models

# Create your models here.
class contact_form_details(models.Model):
    name = models.CharField(max_length=512)
    contact = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    is_contacted = models.BooleanField(default=False)