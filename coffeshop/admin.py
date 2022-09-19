from django.contrib import admin
from coffeshop.models import User
# Register your models here.
"""We are adding the CRUD options to admin pre-built dashboard"""
admin.site.register(User)