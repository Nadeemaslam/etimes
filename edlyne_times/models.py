from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.core.files.storage import FileSystemStorage

from django.db import models
fs = FileSystemStorage(location='/tmp')
CHOICES = (
        ('dividend', 'Dividend Report'),
        ('gold', 'Gold Report'),
        ('penny', 'Penny Report'),
        ('resources', 'Resources Report'),
        ('health', 'Health Care Report'),
        ('platinum', 'Platinum Report'),
    )

class report(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default=None, unique=True)
    exchange = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CHOICES, default=None, blank=True, null=True)
    file = models.FileField(storage=fs)
