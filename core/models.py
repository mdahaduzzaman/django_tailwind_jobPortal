import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# A utility function for uploading User avatar
def user_avatar_upload_path(instance, filename):
    return f'User/Avatar/{instance.full_name}_{instance.id}_{filename}'

# A utility function for uploading user cv
def user_cv_upload_path(instance, filename):
    return f'JobSeeker/CV/{instance.user.full_name}_{instance.id}_{filename}'

# A utility function for uploading company image
def company_image_upload_path(instance, filename):
    return f'Company/Logo/{instance.company_name}_{instance.user.id}_{filename}'

# Creating a CustomUserManager for manage the CustomUser
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(upload_to=user_avatar_upload_path, blank=True, null=True, verbose_name=_('Avatar'))
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    full_name = models.CharField(max_length=255, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'User'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

class Recruiter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, verbose_name=_('Company Name'))
    company_address = models.TextField(verbose_name=_('Company Address'))
    company_about = models.TextField(verbose_name=_('About Company'))
    company_logo = models.ImageField(upload_to=company_image_upload_path, verbose_name=_('Company Logo'))
    total_employees = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.company_name
    
    class Meta:
        db_table = "Recruiter"
        verbose_name = _('Recruiter')
        verbose_name_plural = _('Recruiters')


class Skill(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Skill Name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "Skill"
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

class JobSeeker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cv = models.FileField(upload_to=user_cv_upload_path, blank=True, null=True, verbose_name=_('CV'))
    skills = models.ManyToManyField(Skill)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.full_name
    
    class Meta:
        db_table = "JobSeeker"
        verbose_name = _('JobSeeker')
        verbose_name_plural = _('JobSeekers')


class Applicationjobseeker(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    jobpost = models.OneToOneField('JobPost', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.full_name
    
    class Meta:
        db_table = "Applicationjobseeker"
        verbose_name = _('Applicationjobseeker')
        verbose_name_plural = _('Applicationjobseekers')

class JobPost(models.Model):
    jobs = (
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    position = models.CharField(max_length=150)
    about_this_job = models.TextField()
    job_responsibilities = models.TextField()
    job_requirements = models.TextField()
    salary = models.IntegerField()
    location = models.TextField()
    skills_required = models.ManyToManyField(Skill)
    job_type = models.CharField(max_length=20, choices = jobs, default='Onsite')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.position
    
    class Meta:
        db_table = "JobPost"
        verbose_name = _('JobPost')
        verbose_name_plural = _('JobPosts')