from django.contrib import admin

# Register your models here.

from .models import Company,Resume

admin.site.register(Company)
admin.site.register(Resume)