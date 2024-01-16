from .models import *
from django.contrib.auth.forms import UserCreationForm
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

    
    class Meta:
        model = JobSeeker
        exclude = ('user',)

class UserProfileEditForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['full_name', 'avatar']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter position", 'autofocus': 'autofocus'}),

            'avatar': forms.FileInput(attrs={'class': 'shadow-sm block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}),
        }
    

class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude = ('user',)
        

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter company name"}),

            'company_address': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter company address", 'rows': "3"}),

            'company_about': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter company about", 'rows': "3"}),

            'company_logo': forms.FileInput(attrs={'class': 'shadow-sm block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}),

            'company_cover_photo': forms.FileInput(attrs={'class': 'shadow-sm block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}),

            # 'total_employees': forms.NumberInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter total number of employees"}),

            'website': forms.URLInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter website url"}),

            'main_services': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter main service"}),
        }
    total_employees = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter total number of employees"}))
    


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        exclude = ('user',)
        widgets = {
            'cv': forms.FileInput(attrs={'class': 'shadow-sm block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}),

            'cover_photo': forms.FileInput(attrs={'class': 'shadow-sm block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}),

            'headline': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter your headline"}),

            'about': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter about yourself", 'rows': "3"}),

            'location': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter your location", 'rows': "3"}),

            

            'skills': forms.CheckboxSelectMultiple(attrs={'class': 'w-48 text-sm px-2 text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'}),

        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['position', 'company_name', 'from_time', 'to_time', 'job_type', 'job_time', 'details_of_this_job']
        widgets = {
            'position': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter your position"}),

            'company_name': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter your company name"}), 

            'from_time': forms.DateInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'type': 'date'}), 

            'to_time': forms.DateInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'type': 'date'}), 

            'job_type': forms.Select(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter position"}), 

            'job_time': forms.Select(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter position"}), 

            'details_of_this_job': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter details of this position", 'rows': "3"})
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'start_date', 'end_date', 'field_of_study']
        widgets = {
            'school': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter your position"}),

            'degree': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter your company name"}), 

            'start_date': forms.DateInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'type': 'date'}), 

            'end_date': forms.DateInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'type': 'date'}), 

            'field_of_study': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter your company name"}), 
        }
class JobPostForm(forms.ModelForm):
    new_skills = forms.CharField(
        required=False,
        help_text="Enter new skills, separated by commas.",
        widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter new skills, separated by commas."})
    )
    class Meta:
        model = JobPost
        fields = ['position', 'number_of_vacancies', 'salary', 'job_type', 'deadline', 'skills_requied', 'new_skills', 'about_this_job']
        # exclude = ('recruiter', 'is_active')

        widgets = {
            'position': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:bg-white focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter position", 'autofocus': 'autofocus'}),

            # 'about_this_job': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter about of this position", 'rows': "3"}),

            # 'job_responsibilities': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter responsibilities of this position", 'rows': "3"}),

            # 'job_requirements': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter requirements of this position", 'rows': "3"}),

            'salary': forms.NumberInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter salary or leave blank for negotiable"}),

            'number_of_vacancies': forms.NumberInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter number of vacancy"}),

            'location':forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': "Enter location", 'rows': "3"}),

            'skills_requied': forms.SelectMultiple(attrs={'class': 'w-full rounded-lg border-0 outline-0'}),

            'job_type': forms.Select(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter position"}),

            'deadline': forms.DateTimeInput(attrs={
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'type': 'datetime-local'
            })
        }

    salary = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light', 'placeholder': "Enter salary or leave blank for negotiable"}))

    def clean(self):
        cleaned_data = super().clean()

        # Process existing skills
        skills_existing = cleaned_data.get('skills_requied')
        
        # Process new skills
        new_skills_str = cleaned_data.get('new_skills')
        new_skills_list = [skill.strip() for skill in new_skills_str.split(',') if skill.strip()]

        # Check if skills_existing is not None before trying to use it
        if skills_existing is None:
            skills_existing = []  # or skills_existing = []

        # Convert QuerySet to list
        skills_existing_list = list(skills_existing)

        # Create new skills and add them to the cleaned_data
        new_skills_objects = []
        
        for new_skill in new_skills_list:
            skill, created = Skills.objects.get_or_create(name=new_skill)
            new_skills_objects.append(skill)

        # Combine existing skills and new skills
        combined_skills = skills_existing_list + new_skills_objects
        cleaned_data['skills_requied'] = combined_skills

        return cleaned_data


class TestForm(forms.ModelForm):
    new_skills = forms.CharField(
        required=False,
        help_text="Enter new skills, separated by commas."
    )

    class Meta:
        model = JobPost
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        # Process existing skills
        skills_existing = cleaned_data.get('skills_requied')
        
        # Process new skills
        new_skills_str = cleaned_data.get('new_skills')
        new_skills_list = [skill.strip() for skill in new_skills_str.split(',') if skill.strip()]

        # Check if skills_existing is not None before trying to use it
        if skills_existing is None:
            skills_existing = []  # or skills_existing = []

        # Convert QuerySet to list
        skills_existing_list = list(skills_existing)

        # Create new skills and add them to the cleaned_data
        new_skills_objects = []
        
        for new_skill in new_skills_list:
            skill, created = Skills.objects.get_or_create(name=new_skill)
            new_skills_objects.append(skill)

        # Combine existing skills and new skills
        combined_skills = skills_existing_list + new_skills_objects
        cleaned_data['skills_requied'] = combined_skills

        return cleaned_data
