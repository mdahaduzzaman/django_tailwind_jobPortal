import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from .forms import *
from .utils import *

def home(request):
    jobs = JobPost.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'core/home.html', {'jobs': jobs})


def add_job_post(request):
    if request.method == "POST":
        # form = JobPostForm(request.POST)
        form = JobPostForm(request.POST)
        if form.is_valid():
            try:
                form.instance.recruiter = request.user.recruiter
                form.save()
                messages.success(request, 'Job added successfully')
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Post not added for {e}")
    else:
        form = JobPostForm()
    return render(request, 'core/add_job_post.html', {'form': form})

def edit_job_post(request, jobPostID):
    jobPostInstance = JobPost.objects.get(pk=jobPostID)

    if request.method == "POST":
        form = JobPostForm(request.POST, instance=jobPostInstance)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Job edited successfully')
                return redirect('home')
            except:
                messages.error(request, "You don't have permission to edit a job")
    else:
        form = JobPostForm(instance=jobPostInstance)
    return render(request, 'core/add_job_post.html', {'form': form})

def delete_job_post(request, jobPostID):
    jobPostInstance = JobPost.objects.get(pk=jobPostID)

    jobPostInstance.is_active = False
    messages.success(request, f'Job post deleted successfully with positin {jobPostInstance.position}.')
    jobPostInstance.save()
    return redirect('home')


def search(request):
    content = request.GET.get('search')

    try:
        recruiter = request.user.recruiter
        users = CustomUser.objects.filter(jobseeker__isnull=False, jobseeker__skills__name__icontains=content)
        return render(request, 'core/professionals.html', {'users': users})
    except:
        jobs = JobPost.objects.filter(position__icontains=content) | JobPost.objects.filter(about_this_job__icontains=content)

        return render(request, 'core/home.html', {'jobs': jobs})


def details_job(request, jobId):
    job = JobPost.objects.get(pk=jobId)
    return render(request, 'core/details_job.html', {'job': job})

def apply_job(request, jobpostID):
    if request.user.is_authenticated:
        jobpost = JobPost.objects.get(pk=jobpostID)
        if user_is_jobseeker(request.user):
            try:
                application = Applicationjobseeker.objects.get(jobseeker=request.user.jobseeker)
                messages.success(request, "You've already applied.")
            except:
                application = Applicationjobseeker(jobseeker=request.user.jobseeker, jobpost=jobpost)
                application.save()
                messages.success(request, 'Successfully applied.')
            pass
        else:
            if user_is_recruiter(request.user):
                if request.user.recruiter == jobpost.recruiter:
                    messages.warning(request, "This job is posted by you")

        # Redirect to where the request is generated
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "You have to login first to apply")
        return redirect('user_login')

def recruiters_list(request):
    recruiters = Recruiter.objects.all()
    return render(request, 'core/recruiters_list.html', {'recruiters': recruiters})


def details_recruiter(request, recruiterID):

    recruiters = Recruiter.objects.all()

    recruiter = get_object_or_404(recruiters, pk=recruiterID)
    recruiters = recruiters.exclude(pk=recruiter.pk)

    jobs = recruiter.jobpost_set.all()

    return render(request, 'core/details_recruiter.html', {'recruiters': recruiters, 'recruiter': recruiter, 'jobs': jobs})

def professionals(request):
    users = CustomUser.objects.filter(jobseeker__isnull=False).order_by('-date_joined')

    return render(request, 'core/professionals.html', {'users': users})

def professional(requset, userId):
    users = CustomUser.objects.filter(jobseeker__isnull=False)

    user = get_object_or_404(users, pk=userId)
    users = users.exclude(pk=user.pk)

    return render(requset, 'core/professional.html', {'user': user, 'users': users})

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('dashboard')
                # return redirect('dashboard')
        else:
            form = SignupForm()
        return render(request, 'core/user_signup.html', {'form': form})
    else:
        return redirect('dashboard')
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully.")
                    return redirect('dashboard')
                else:
                    messages.error(request, "Invalid credential")
        else:
            form = LoginForm()
        return render(request, 'core/user_login.html', {'form': form})
    else:
        return redirect('dashboard')

def user_logout(request):
    logout(request)
    return redirect('user_login')

def dashboard(request):
    user = request.user
    context ={}

    # if user is jobseeker then including this jobseeker object
    if user_is_jobseeker(user):
        context['applications'] = user.jobseeker.applicationjobseeker_set.all()
        context['jobseeker'] = user.jobseeker
        return render(request, 'core/dashboard.html', context)



    # if user is recruiter then including this recruiter object
    if user_is_recruiter(user):
        count = 0
        jobs = user.recruiter.jobpost_set.filter(is_active=True).order_by('-created_at')

        # Getting total number of application count
        for jobpost in jobs:
            for _ in jobpost.applicationjobseeker_set.all():
                count += 1

        context['jobs'] = jobs
        context['recruiter'] = user.recruiter
        context['applications'] = True if jobs else False
        context['applicationCount'] = count

        return render(request, 'core/dashboard.html', context)
    
    return redirect('joinas')

def profile(request):
    user = request.user
    context = {}
    context['profileUpdateForm'] = UserProfileEditForm(instance=user)

    # if the user is jobseeker then including this jobseeker object
    if user_is_jobseeker(user):
        context['jobseekerUpdateForm'] = JobSeekerForm(instance=user.jobseeker)
        context['experienceUpdateForm'] = ExperienceForm()
        context['educationUpdateForm'] = EducationForm()    
        
    # if the user is recruiter then including this recruiter object
    if user_is_recruiter(user):
        context['recruiterUpdateForm'] = RecruiterForm(instance=user.recruiter)

    return render(request, 'core/profile.html', context)

def update_profile(request):
    if request.method == "POST":
        profileUpdateForm = UserProfileEditForm(request.POST, request.FILES, instance=request.user)

        if profileUpdateForm.is_valid():
            profileUpdateForm.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, f"{dict(profileUpdateForm.errors.items())}")
    return redirect('profile')


def update_recruiter_profile(request):
    if request.method == "POST":

        recruiterUpdateForm = RecruiterForm(request.POST, request.FILES, instance=request.user.recruiter)
        if recruiterUpdateForm.is_valid():
            recruiterUpdateForm.save()
            messages.success(request, f"{request.user.recruiter.company_name} updated successfully")
        else:
            messages.error(request, f"{dict(recruiterUpdateForm.errors.items())}")
    return redirect('profile')


def update_jobseeker_profile(request):
    if request.method == "POST":

        jobseekerUpdateForm = JobSeekerForm(request.POST, request.FILES, instance=request.user.jobseeker)
        if jobseekerUpdateForm.is_valid():
            jobseekerUpdateForm.save()
            messages.success(request, f"{request.user.jobseeker.headline} updated successfully")
        else:
            messages.error(request, f"{dict(jobseekerUpdateForm.errors.items())}")
    return redirect('profile')

def add_experience(request):
    if user_is_jobseeker(request.user):
        if request.method == "POST":
            experienceUpdateForm = ExperienceForm(request.POST)
            if experienceUpdateForm.is_valid():
                experienceUpdateForm.instance.jobseeker = request.user.jobseeker
                obj = experienceUpdateForm.save()
                messages.success(request, f"{obj.jobseeker.user.full_name} experience added successfully")
            else:
                messages.error(request, f"{dict(experienceUpdateForm.errors.items())}")
        return redirect('profile')
    else:
        messages.error(request, "Without jobseeker account, You will not be able to add experience")
        return redirect('dashboard')

def update_experience(request, experienceID):
    if request.method == "POST":
        experienceObject = Experience.objects.get(pk=experienceID)
        if experienceObject.jobseeker.user == request.user:
            experienceUpdateForm = ExperienceForm(request.POST, request.FILES, instance=experienceObject)
            if experienceUpdateForm.is_valid():
                experienceUpdateForm.instance.jobseeker = request.user.jobseeker
                obj = experienceUpdateForm.save()
                messages.success(request, f"{obj.jobseeker.user.full_name} experience updated successfully")
            else:
                messages.error(request, f"{dict(experienceUpdateForm.errors.items())}")
        else:
            messages.error(request, "You aren't authorized to update this experience")
    return redirect('profile')


def delete_experience(request, experienceID):
    obj = Experience.objects.get(pk=experienceID)
    if obj.jobseeker.user == request.user:
        obj.delete()
        messages.success(request, 'Experience deleted successfully')
    else:
        messages.error(request, "You aren't authorized to delete this experience")
    return redirect('profile')

def add_education(request):
    if user_is_jobseeker(request.user):
        if request.method == "POST":
            educationUpdateForm = EducationForm(request.POST)
            if educationUpdateForm.is_valid():
                educationUpdateForm.instance.jobseeker = request.user.jobseeker
                obj = educationUpdateForm.save()
                messages.success(request, f"{obj.jobseeker.user.full_name} education added successfully")
            else:
                messages.error(request, f"{dict(educationUpdateForm.errors.items())}")
        return redirect('profile')
    else:
        messages.error(request, "Without jobseeker account, You will not be able to add education")
        return redirect('dashboard')

def update_education(request, educationID):
    if request.method == "POST":
        educationObject = Education.objects.get(pk=educationID)

        if educationObject.jobseeker.user == request.user:
            educationUpdateForm = EducationForm(request.POST, request.FILES, instance=educationObject)
            if educationUpdateForm.is_valid():
                educationUpdateForm.instance.jobseeker = request.user.jobseeker
                obj = educationUpdateForm.save()
                messages.success(request, f"{obj.jobseeker.user.full_name} education updated successfully")
            else:
                messages.error(request, f"{dict(educationUpdateForm.errors.items())}")
        else:
            messages.error(request, "You aren't authorized to update this education")
    return redirect('profile')


def delete_education(request, educationID):
    obj = Education.objects.get(pk=educationID)
    if obj.jobseeker.user == request.user:
        obj.delete()
        messages.success(request, 'Education deleted successfully')
    else:
        messages.error(request, "You aren't authorized to delete this education")
    return redirect('profile')


def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def joinas(request):
    if request.user.is_authenticated:
        return render(request, 'core/joinas.html')
    else:
        return redirect('user_login')

def register_profile(request, type):
    form = None
    register_type = None
    if type=='recruiter':
        if request.method == "POST":
            form = RecruiterForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                messages.success(request, 'Recruiter account created successfully.')
                form.save()
                recruiter = Group.objects.get(name='Recruiter')
                request.user.groups.add(recruiter)
                return redirect('dashboard')
        else:
            form = RecruiterForm()
        register_type = "Reqruiter"
    elif type=="jobseeker":
        if request.method == "POST":
            form = JobseekerForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                messages.success(request, 'Jobseeker account created successfully.')
                form.save()
                jobseeker = Group.objects.get(name='Jobseeker')
                request.user.groups.add(jobseeker)
                return redirect('dashboard')
        else:
            form = JobseekerForm()
        register_type = "Job Seeker"
    else:
        return redirect('home')
    return render(request, 'core/register_profile.html', {'form': form, 'register_type': register_type})


# ACCEPT BUTTON FOR RECRUITER
def accept_application(request, pk):
    application = Applicationjobseeker.objects.get(pk=pk)
    application.status = "Accepted"
    messages.success(request, 'Accepted successfully')
    application.save()

    return redirect(request.META.get('HTTP_REFERER'))

# ACCEPT BUTTON FOR RECRUITER
def decline_application(request, pk):
    application = Applicationjobseeker.objects.get(pk=pk)
    application.status = "Declined"
    messages.success(request, 'Declined successfully')
    application.save()

    return redirect(request.META.get('HTTP_REFERER'))