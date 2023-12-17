from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# A utility function for uploading User avatar
def user_avatar_upload_path(instance, filename):
    return f'User/Avatar/{instance.username}_{instance.id}_{filename}'

# A utility function for uploading user cv
def user_cv_upload_path(instance, filename):
    return f'User/CV/{instance.username}_{instance.id}_{filename}'

# A utility function for uploading company image
def company_image_upload_path(instance, filename):
    return f'Company/Logo/{instance.company_name}_{instance.user.id}_{filename}'


class CustomUser(AbstractUser, PermissionsMixin):
    avatar = models.ImageField(upload_to=user_avatar_upload_path, blank=True, null=True, verbose_name=_('Avatar'))
    cv = models.FileField(upload_to=user_cv_upload_path, blank=True, null=True, verbose_name=_('CV'))

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

class Recruiter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, verbose_name=_('Company Name'))
    company_address = models.CharField(max_length=255, verbose_name=_('Company Address'))
    company_about = models.TextField(verbose_name=_('About Company'))
    company_logo = models.ImageField(upload_to=company_image_upload_path, verbose_name=_('Company Logo'))

    def __str__(self) -> str:
        return self.company_name
    
    class Meta:
        verbose_name = _('Recruiter')
        verbose_name_plural = _('Recruiters')