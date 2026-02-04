from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User

class UserAdmin(BaseAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ["email", "username", "first_name", "last_name", "phone", 'address', "is_staff", "is_active"]
    search_fields = ["email", "username", "first_name", "last_name", "phone"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    ordering = ["email"]

    fieldsets = BaseAdmin.fieldsets + ((None, {'fields': ('phone', 'address',)}),)
    add_fieldsets = BaseAdmin.add_fieldsets + ((None, {'fields': ('phone', 'address',)}),)

admin.site.register(User, UserAdmin)
