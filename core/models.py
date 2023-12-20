import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

# A utility function for uploading User avatar
def user_avatar_upload_path(instance, filename):
    return f'User/Avatar/{instance.full_name}_{instance.id}_{filename}'

# A utility function for uploading user cv
def user_cv_upload_path(instance, filename):
    return f'JobSeeker/CV/{instance.user.full_name}_{instance.id}_{filename}'

# A utility function for uploading company image
def company_image_upload_path(instance, filename):
    return f'Company/Logo/{instance.company_name}_{instance.id}_{filename}'

# A utility function for uploading company image
def company_cover_image_upload_path(instance, filename):
    return f'Company/CoverPhoto/{instance.company_name}_{instance.id}_{filename}'

# A utility function for uploading jobseeker cover image
def cover_photo_upload_path(instance, filename):
    return f'JobSeeker/CoverPhoto/{instance.user.full_name}_{instance.id}_{filename}'

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

    def save(self, *args, **kwargs):
        if self._state.adding:  # Check if the instance is being added (created) for the first time
            self.password = make_password(self.password)  # Hash the password using Django's make_password
        return super().save(*args, **kwargs)

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
    company_cover_photo = models.ImageField(upload_to=company_cover_image_upload_path, verbose_name=_('Company Cover Photo'), null=True)
    total_employees = models.IntegerField(default=0)
    website = models.URLField(null=True)
    main_services = models.CharField(max_length=150, null=True)

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
    cover_photo = models.ImageField(upload_to=cover_photo_upload_path, blank=True, null=True)
    about = models.TextField(null=True)
    headline = models.CharField(max_length=100, null=True)
    skills = models.ManyToManyField(Skill)
    location = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.full_name
    
    class Meta:
        db_table = "JobSeeker"
        verbose_name = _('JobSeeker')
        verbose_name_plural = _('JobSeekers')

class Experience(models.Model):
    jobs = (
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote'),
    )
    time = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    position = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    from_time = models.DateField()
    to_time = models.DateField()
    job_type = models.CharField(max_length=15, choices=jobs, default="Onsite")
    job_time = models.CharField(max_length=15, choices=time, default="Full-time")
    details_of_this_job = models.TextField()
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.jobseeker.user.full_name
    
    class Meta:
        db_table = "Experience"
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')


class Education(models.Model):
    school = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    field_of_study = models.CharField(max_length=150)
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.school
    
    class Meta:
        db_table = "Education"
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')
    

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
    deadline = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.position
    
    class Meta:
        db_table = "JobPost"
        verbose_name = _('JobPost')
        verbose_name_plural = _('JobPosts')