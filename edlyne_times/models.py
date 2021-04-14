from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.core.files.storage import FileSystemStorage

from django.db import models
fs = FileSystemStorage(location='static/edlyne_times/files')

class report(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default=None, unique=True)
    exchange = models.CharField(max_length=255)
    file = models.FileField(storage=fs)
