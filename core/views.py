from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import *
from .utils import *

def home(request):
    jobs = JobPost.objects.all()
    return render(request, 'core/home.html', {'jobs': jobs})

def search(request):
    content = request.GET.get('search')
    print(content)
    try:
        recruiter = request.user.recruiter
        users = CustomUser.objects.filter(jobseeker__isnull=False, jobseeker__skills__name__icontains=content)
        return render(request, 'core/professionals.html', {'users': users})
    except:
        try:
            jobseeker = request.user.jobseeker

            jobs = JobPost.objects.filter(skills_required__name__icontains=content)
            return render(request, 'core/home.html', {'jobs': jobs})
        except:
            return redirect('home')


def details_job(request, jobId):
    job = JobPost.objects.get(pk=jobId)
    return render(request, 'core/details_job.html', {'job': job})

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
    users = CustomUser.objects.filter(jobseeker__isnull=False)

    return render(request, 'core/professionals.html', {'users': users})

def professional(requset, userId):
    users = CustomUser.objects.all()

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
    user = request.user
    context ={}

    # if user is jobseeker then including this jobseeker object
    if user_is_jobseeker(user):
        context['applications'] = user.jobseeker.applicationjobseeker_set.all()
        context['jobseeker'] = user.jobseeker

    # if user is recruiter then including this recruiter object
    if user_is_recruiter(user):
        count = 0
        for jobpost in user.recruiter.jobpost_set.all():
            for application in jobpost.applicationjobseeker_set.all():
                count += 1

        jobs = user.recruiter.jobpost_set.all()
        context['jobs'] = jobs
        context['recruiter'] = user.recruiter
        context['applicationCount'] = count

    return render(request, 'core/dashboard.html', context)


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