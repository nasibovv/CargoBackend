from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    row_status = models.IntegerField(default = 1)
    
class PhonePrefix(models.Model):
    phone_prefix = models.CharField(max_length=7)
    row_status = models.IntegerField(default = 1)

'''
    0 - 100qr	1.79$   --> id = 1
101qr - 250qr	2.49$   --> id = 2
251qr - 500qr	3.49$   --> id = 3
501qr - 1kg	    3.83$   --> id = 4
1kg üzərində	x3.83$  --> id = 5

'''
class Tariff(models.Model):
    weight_range = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    base_price = models.DecimalField(decimal_places=2, max_digits=3)
    is_fixed = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)]) # 1-per gram; 0 - is fixed
    is_liquid = models.BooleanField()
    show_order = models.IntegerField()
