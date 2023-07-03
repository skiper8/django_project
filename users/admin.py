from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'country', 'is_active', 'token')
    search_fields = ('country', 'first_name',)
    list_filter = ('country',)
