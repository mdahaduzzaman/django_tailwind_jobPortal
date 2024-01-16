from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('update-profile/', update_profile, name='update_profile'),
    path('update-recruiter-profile/', update_recruiter_profile, name='update_recruiter_profile'),
    path('update-jobseeker-profile/', update_jobseeker_profile, name='update_jobseeker_profile'),

    path('add-experience/', add_experience, name='add_experience'),
    path('update-experience/<str:experienceID>', update_experience, name='update_experience'),
    path('delete-experience/<str:experienceID>', delete_experience, name='delete_experience'),

    path('add-education/', add_education, name='add_education'),
    path('update-education/<str:educationID>', update_education, name='update_education'),
    path('delete-education/<str:educationID>', delete_education, name='delete_education'),

    path('add-job/', add_job_post, name='add_job_post'),
    path('edit-job/<str:jobPostID>', edit_job_post, name='edit_job_post'),
    path('delete-job/<str:jobPostID>', delete_job_post, name='delete_job_post'),
    path('search/', search, name='search'),
    path('details-job/<str:jobId>', details_job, name='details_job'),
    path('apply-job/<str:jobpostID>', apply_job, name='apply_job'),
    path('recruiters-list/', recruiters_list, name='recruiters_list'),
    path('details-recruiter/<str:recruiterID>', details_recruiter, name='details_recruiter'),

    path('user-signup/', user_signup, name='user_signup'),
    path('user-login/', user_login, name='user_login'),
    path('user-logout/', user_logout, name='user_logout'),

    path('dashboard/', dashboard, name='dashboard'),
    path('professional/<str:userId>', professional, name='professional'),
    path('professionals/', professionals, name='professionals'),

    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('join-as/', joinas, name='joinas'),
    path('register-profile/<str:type>', register_profile, name='register_profile'),


    path('accept-application/<int:pk>', accept_application, name='accept_application'),
    path('decline-application/<int:pk>', decline_application, name='decline_application'),


]
