from django.db import models

# Create your models here.
from django.db import models

class EmailSubscriber(models.Model):
    email = models.EmailField()
    created_at = models.DateField()