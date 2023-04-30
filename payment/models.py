from django.db import models
from user.models import User



class Currency(models.Model):
    currency_name = models.CharField(max_length=5)
    currency_sign = models.CharField(max_length=1)
    currency_rate = models.DecimalField()


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=5, decimal_places=2)

    