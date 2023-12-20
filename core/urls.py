from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('details-job/<str:jobId>', details_job, name='details_job'),
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
]
