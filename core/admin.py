from django.contrib import admin
from core.models import Country, PhonePrefix, Tariff


admin.site.register(Country)
admin.site.register(PhonePrefix)
admin.site.register(Tariff)


