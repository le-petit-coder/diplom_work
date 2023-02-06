from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_filter = ['email', 'first_name', 'last_name', 'username']
