from django.contrib import admin
from faq.models import FAQ_category, FAQ

admin.site.register(FAQ_category)
admin.site.register(FAQ)
