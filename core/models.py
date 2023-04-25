from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    row_status = models.IntegerField(default = 1)
    
class PhonePrefix(models.Model):
    phone_prefix = models.CharField(max_length=7)
    row_status = models.IntegerField(default = 1)