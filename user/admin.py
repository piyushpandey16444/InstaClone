from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_superuser', 'is_active', 'first_name']
    list_display_links = ['username',
                          'is_superuser', 'is_active', 'first_name']
