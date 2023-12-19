from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class SignupForm(UserCreationForm):
    full_name = forms.CharField(label='Full Name', max_length=100, required=True, error_messages={'required': 'Name is required'})
    email = forms.EmailField(label='Email', max_length=254, required=True, error_messages={'required': 'Email is required'})
    password1 = forms.CharField(label="Password", required=True, error_messages={'required': 'Password must be set'}, widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password", required=True, error_messages={'required': 'Confirm password must be set'}, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'avatar']

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254, required=True, error_messages={'required': 'Email is required'})
    password = forms.CharField(label="Password", required=True, error_messages={'required': 'Password must be set'}, widget=forms.PasswordInput())

class JobseekerForm(forms.ModelForm):
    cv = forms.FileField(
        label="Upload your CV",
        widget=forms.ClearableFileInput(attrs={'class': ''}),
        required=True, 
        error_messages={'required': 'CV is required'}
    )

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),  # Replace Skill.objects.all() with your queryset
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'your-custom-class'}),
        label="Select your skills",
        error_messages={'required': 'Please select at least one skill'}, required=True
    )
    
    class Meta:
        model = JobSeeker
        exclude = ('user',)

class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude = ('user',)

class JobPostForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),  # Replace Skill.objects.all() with your queryset
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'your-custom-class'}),
        label="Select skills",
        error_messages={'required': 'Please select at least one skill'}, required=True
    )
    class Meta:
        model = JobPost
        exclude = ('recruiter',)
        