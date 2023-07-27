from django.contrib import admin

# Register your models here.
from .models.user import User


admin.site.register(User)
