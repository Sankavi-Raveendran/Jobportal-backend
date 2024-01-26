from django.db import models


class jobs(models.Model):
    name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    companyname = models.CharField(max_length = 255)
  




