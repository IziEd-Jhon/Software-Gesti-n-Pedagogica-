from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.


#  Profile
class customUser(AbstractBaseUser, PermissionsMixin):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)             # para extender el usuario base
    deleted     = models.BooleanField(default=False)    #  Opcional
    suspended   = models.BooleanField(default=False)    #  Opcional
    username    = models.CharField(max_length=150, blank=False, unique=True) # Puede que se use el de OAuth
    firstname   = models.CharField(max_length=100, default='', blank=True, null=True)
    lastname    = models.CharField(max_length=100, default='', blank=True, null=True)
    email       = models.EmailField(max_length=100, unique=True, blank=True, default='')
    birthdate   = models.DateField(null=True, blank=True)
    phonel      = models.CharField(max_length=20, default='', blank=True, null=True)
    phone2      = models.CharField(max_length=20, default='', blank=True, null=True)
    institution = models.CharField(max_length=255, default='', blank=True, null=True)
    department  = models.CharField(max_length=255, default='', blank=True, null=True)
    address     = models.CharField(max_length=255, default='', blank=True, null=True)
    city        = models.CharField(max_length=120, default='', blank=True, null=True)
    firstlogin  = models.DateTimeField(null=True, blank=True)
    lastlogin   = models.DateTimeField(null=True, blank=True)
    lastip      = models.CharField(max_length=45, default='', blank=True, null=True)
    picture     = models.BigIntegerField(default=0, blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)
    timecreated = models.DateTimeField(auto_now_add=True, editable=False)
    timemodified= models.DateTimeField(auto_now=True)
    imagealt    = models.CharField(max_length=255, default='', blank=True, null=True)

    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)
    last_login  = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
        (3, 'parent'),
        (4, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['password', 'email']

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    #En settings.py cambiar AUTH_USER_MODEL = 'customUser'


class Teacher(customUser):
    tittles         = models.TextField()
    experience      = models.TextField()

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

class Parent(customUser):
    alumnos         = models.ForeignKey(customUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='customUser_alumnos')

    class Meta:
        verbose_name = "Apoderado"
        verbose_name_plural = "Apoderados"