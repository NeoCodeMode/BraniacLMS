from django.contrib import admin

from authapp import forms, models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = forms.CustomUserChangeForm
    form_add = forms.CustomUserCreationForm
    list_display = ["id", "username", "email", "is_active", "date_joined"]
    ordering = ["-date_joined"]
