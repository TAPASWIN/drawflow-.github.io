from django.db import models

# Create your models here.
# configurator/models.py


class ComputerConfiguration(models.Model):
    json_config = models.JSONField()
    address = models.CharField(max_length=255)

