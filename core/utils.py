from django.contrib.auth.models import Group

def user_is_jobseeker(user):
    try:
        jobseeker_group = Group.objects.get(name='Jobseeker')
        return jobseeker_group in user.groups.all()
    except Group.DoesNotExist:
        return False

def user_is_recruiter(user):
    try:
        recruiter_group = Group.objects.get(name='Recruiter')
        return recruiter_group in user.groups.all()
    except Group.DoesNotExist:
        return False
