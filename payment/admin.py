from django.contrib import admin
from payment.models import  Currency, Wallet

admin.site.register(Currency)
admin.site.register(Wallet)

