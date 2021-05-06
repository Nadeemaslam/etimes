from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    message = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email
