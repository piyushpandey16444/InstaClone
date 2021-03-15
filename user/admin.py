from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username', 'is_superuser', 'is_active']
    list_display_links = ['full_name', 'username',
                          'is_superuser', 'is_active']
