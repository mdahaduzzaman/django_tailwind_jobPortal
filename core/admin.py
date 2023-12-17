from django.contrib import admin
from .models import CustomUser, Recruiter

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    readonly_fields = ('password',)

@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'company_address', 'user')
    search_fields = ('company_name', 'company_address', 'user__username')
    list_filter = ('company_name', 'company_address')
