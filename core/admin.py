from django.contrib import admin
from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'company_address', 'user')
    search_fields = ('company_name', 'company_address', 'user__username')
    list_filter = ('company_name', 'company_address')

@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user', 'skills')
    list_filter = ('user', 'skills')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Applicationjobseeker)
class ApplicationjobseekerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'jobpost')
    search_fields = ('user', 'jobpost')

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'recruiter', 'job_type')
    search_fields = ('position', 'recruiter', 'job_type')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'company_name', 'job_type')
    search_fields = ('position', 'company_name', 'job_type')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'degree', 'field_of_study')
    search_fields = ('school', 'degree', 'field_of_study')