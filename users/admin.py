from django.contrib import admin

from users.models import User


@admin.register(User)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar', 'phone', 'country')
