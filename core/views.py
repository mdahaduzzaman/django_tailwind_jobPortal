from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *

def home(request):
    jobs = JobPost.objects.all()
    return render(request, 'core/home.html', {'jobs': jobs})

def details_job(request, jobId):
    job = JobPost.objects.get(pk=jobId)
    return render(request, 'core/details_job.html', {'job': job})

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
                if user:
                    messages.success(request, "Logged in successfully.")
                    login(request, user)
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
    context ={}
    reqruiter_instance = None
    jobseeker_instance = None
    if request.user.is_authenticated:
        user = request.user

        # Trying to find that the user type
        try:
            reqruiter_instance = user.recruiter
        except:
            try:
                jobseeker_instance = user.jobseeker
            except:
                return redirect('joinas')
        if reqruiter_instance:
            pass
            # form = JobPostForm()
            # context = {
            #     'form': form,

            # }
        elif jobseeker_instance:
            context = {}
        return render(request, 'core/dashboard.html', context)
    else:
        return redirect('user_login')


def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def joinas(request):
    return render(request, 'core/joinas.html')

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
                return redirect('dashboard')
        else:
            form = JobseekerForm()
        register_type = "Job Seeker"
    else:
        return redirect('home')
    return render(request, 'core/register_profile.html', {'form': form, 'register_type': register_type})