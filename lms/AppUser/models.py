from email.policy import default
from pickle import FALSE
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from numpy import NaN
from pandas import DataFrame

from AppCourse.models import Course, Subject

#  Profile
class customUser(AbstractBaseUser, PermissionsMixin):
    deleted     = models.BooleanField(default=False, verbose_name='Borrado')    #  Opcional
    suspended   = models.BooleanField(default=False, verbose_name='Suspendido')    #  Opcional
    username    = models.CharField(max_length=150, blank=False, unique=True, verbose_name='Usuario') # Puede que se use el de OAuth
    firstname   = models.CharField(max_length=100, default='', blank=True, null=True, verbose_name='Nombre')
    lastname    = models.CharField(max_length=100, default='', blank=True, null=True, verbose_name='Apellido')
    email       = models.EmailField(max_length=100, blank=True, default='', verbose_name='Email')
    birthdate   = models.DateField(null=True, blank=True, verbose_name='Cumpleaños')
    phonel      = models.CharField(max_length=20, default='', blank=True, null=True, verbose_name='Celular')
    phone2      = models.CharField(max_length=20, default='', blank=True, null=True, verbose_name='Telefono')
    institution = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name='Institucion')
    department  = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name='Departamento')
    address     = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name='Dirección')
    city        = models.CharField(max_length=120, default='', blank=True, null=True, verbose_name='Ciudad')

    firstlogin  = models.DateTimeField(null=True, blank=True, verbose_name='Primera Conexion')
    lastlogin   = models.DateTimeField(null=True, blank=True, verbose_name='Ultima Conexion')
    lastip      = models.CharField(max_length=45, default='', blank=True, null=True, verbose_name='Ultima IP')
    picture     = models.BigIntegerField(default=0, blank=True, null=True, verbose_name='Imagen')
    description = models.TextField(default='', blank=True, null=True, verbose_name='Descripcion')
    timecreated = models.DateTimeField(auto_now_add=True, editable=False, null=True, verbose_name='Creado')
    timemodified= models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado')
    imagealt    = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name='Imagen Alternativa')

    is_staff    = models.BooleanField(default=False, verbose_name='Staff')
    is_active   = models.BooleanField(default=True, verbose_name='Activo')
    is_superuser= models.BooleanField(default=False, verbose_name='SuperUsuario')
    last_login  = models.DateTimeField(null=True, blank=True, verbose_name='Ultima Conexion2')
    date_joined = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Fecha Creacion')

    class UserTypeChoices(models.IntegerChoices):
        CUSTOM  = 0
        STUDENT = 1
        TEACHER = 2
        PARENT  = 3
        ADMIN   = 4

    user_type = models.PositiveSmallIntegerField(choices=UserTypeChoices.choices, default=UserTypeChoices.STUDENT, verbose_name='Tipo de Usuario')

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

class Annotation(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='customUser_giver')
    #giver   = models.ForeignKey(customUser, on_delete=models.CASCADE, limit_choices_to={'user_type':2}, related_name='customUser_giver')
    #taker   = models.ForeignKey(customUser, on_delete=models.CASCADE, limit_choices_to={'user_type':1}, related_name='customUser_taker')
    student = models.ForeignKey(customUser, on_delete=models.CASCADE, limit_choices_to={'user_type':1}, related_name='customUser_taker')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    comment = models.TextField()
    timecreated     = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    timemodified    = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Anotacion"
        verbose_name_plural = "Anotaciones"

class EnrollmentSubject(models.Model):
    student = models.ForeignKey(customUser, on_delete=models.CASCADE, limit_choices_to={'user_type':1})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status  = models.BooleanField(default=False)
    timecreated     = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    timemodified    = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = [['student', 'subject']]
        verbose_name = "Cursando Materia"
        verbose_name_plural = "Cursando Materias"

class EnrollmentCourse(models.Model):
    student = models.ForeignKey(customUser, on_delete=models.CASCADE, limit_choices_to={'user_type':1})
    course  = models.ForeignKey(Course, on_delete=models.CASCADE)
    status  = models.BooleanField(default=False)
    timecreated     = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    timemodified    = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = [['student', 'course']]
        verbose_name = "Cursando Curso"
        verbose_name_plural = "Cursando Cursos"




DEBUGG_UPLOADFILE = True

def UploadUsersFromFile(reader: DataFrame, update_existing_users=True, create_users=True):
    """
        update_existing_users en True hace que se actualizen los usuarios ya existentes,
        create_users en True hace que se creen los usuarios nuevos,
        combinando ambos se puede setear solo crear, solo updatear o ambos
    """
    list_already_up = []

    # reformat dataframe from posible esp, add every 'verbose_name' : 'field'
    mapped_columns = {}
    for field in customUser._meta.get_fields():
    #change later for user subclass
        if field.concrete and not(
            field.is_relation or field.one_to_one or 
            (field.many_to_one and field.related_model)):
            
            mapped_columns[field.verbose_name.lower()] = field.attname

    reader.columns = reader.columns.str.lower()
    reader.rename(columns=mapped_columns)

    for _, row in reader.iterrows():
        #block of reading values
        
        
        deleted      = False if 'deleted' not in row else (
                        False if not DEBUGG_UPLOADFILE else (
                            False if row.get(['deleted']).isnull().any() else (
                                Boolean(row.get(['deleted']))
                            )))
        suspended      = False if 'suspended' not in row else (
                        False if not DEBUGG_UPLOADFILE else (
                            False if row.get(['suspended']).isnull().any() else (
                                Boolean(row.get(['suspended']))
                            )))
        #deleted      = Boolean(row.get(['deleted'], default=False)) if DEBUGG_UPLOADFILE else False
        #suspended    = Boolean(row.get(['suspended'], default=False)) if DEBUGG_UPLOADFILE else False
        username     = row.get(['username'])
        firstname    = row.get(['username'], default=None)
        lastname     = row.get(['lastname'], default=None)
        email        = row.get(['email'])
        birthdate    = row.get(['birthdate'], default=None)
        phonel       = row.get(['phonel'], default=None)
        phone2       = row.get(['phone2'], default=None)
        institution  = row.get(['institution'], default=None)
        department   = row.get(['department'], default=None)
        address      = row.get(['address'], default=None)
        city         = row.get(['city'], default=None)

        firstlogin   = row.get(['firstlogin'], default=None)
        lastlogin    = row.get(['lastlogin'], default=None)
        lastip       = row.get(['lastip'], default=None)
        picture      = row.get(['picture'], default=None)
        description  = row.get(['description'], default=None)
        timecreated  = row.get(['timecreated'], default=None)
        timemodified = row.get(['timemodified'], default=None)
        imagealt     = row.get(['imagealt'], default=None)

        is_staff     = False if 'is_staff' not in row else (
                        False if not DEBUGG_UPLOADFILE else (
                            False if row.get(['is_staff']).isnull().any() else (
                                Boolean(row.get(['is_staff']))
                            )))
        is_active   = False if 'is_active' not in row else (
                False if not DEBUGG_UPLOADFILE else (
                    False if row.get(['is_active']).isnull().any() else (
                        Boolean(row.get(['is_active']))
                    )))
        is_superuser = False if 'is_superuser' not in row else (
                False if not DEBUGG_UPLOADFILE else (
                    False if row.get(['is_superuser']).isnull().any() else (
                        Boolean(row.get(['is_superuser']))
                    )))                                         
        #is_staff     = Boolean(row.get(['is_staff'], default=False)) if DEBUGG_UPLOADFILE else False
        #is_active    = Boolean(row.get(['is_active'], default=True)) if DEBUGG_UPLOADFILE else True
        #is_superuser = Boolean(row.get(['is_superuser'], default=False)) if DEBUGG_UPLOADFILE else False
        last_login   = row.get(['last_login'], default=None)
        date_joined  = row.get(['date_joined'], default=None)
        
        user_type    = row.get(['user_type'], default=customUser.UserTypeChoices.STUDENT)


       
        user_type = customUser.UserTypeChoices.STUDENT if 'user_type' not in row else (
                customUser.UserTypeChoices.STUDENT if row.get(['is_superuser']).isnull().any()
                    else int(row.get(['user_type']))
                )
        
        if int(user_type) == customUser.UserTypeChoices.ADMIN and not DEBUGG_UPLOADFILE:
            user_type = customUser.UserTypeChoices.CUSTOM

        print("deleted : " + str(deleted) + ", type : " + str(type(deleted))) 
        print("suspended : " + str(suspended) + ", type : " + str(type(suspended))) 
        print("username : " + str(username) + ", type : " + str(type(username))) 
        print("firstname : " + str(firstname) + ", type : " + str(type(firstname))) 
        print("lastname : " + str(lastname) + ", type : " + str(type(lastname))) 
        print("email : " + str(email) + ", type : " + str(type(email))) 
        print("birthdate : " + str(birthdate) + ", type : " + str(type(birthdate))) 
        print("phonel : " + str(phonel) + ", type : " + str(type(phonel))) 
        print("phone2 : " + str(phone2) + ", type : " + str(type(phone2))) 
        print("institution : " + str(institution) + ", type : " + str(type(institution))) 
        print("department : " + str(department) + ", type : " + str(type(department))) 
        print("address : " + str(address) + ", type : " + str(type(address))) 
        print("city : " + str(city) + ", type : " + str(type(city))) 
        print("firstlogin : " + str(firstlogin) + ", type : " + str(type(firstlogin))) 
        print("lastlogin : " + str(lastlogin) + ", type : " + str(type(lastlogin))) 
        print("lastip : " + str(lastip) + ", type : " + str(type(lastip))) 
        print("picture : " + str(picture) + ", type : " + str(type(picture))) 
        print("description : " + str(description) + ", type : " + str(type(description))) 
        print("timecreated : " + str(timecreated) + ", type : " + str(type(timecreated))) 
        print("timemodified : " + str(timemodified) + ", type : " + str(type(timemodified))) 
        print("imagealt : " + str(imagealt) + ", type : " + str(type(imagealt))) 
        print("is_staff : " + str(is_staff) + ", type : " + str(type(is_staff))) 
        print("is_active : " + str(is_active) + ", type : " + str(type(is_active))) 
        print("is_superuser : " + str(is_superuser) + ", type : " + str(type(is_superuser))) 
        print("last_login : " + str(last_login) + ", type : " + str(type(last_login))) 
        print("date_joined : " + str(date_joined) + ", type : " + str(type(date_joined))) 
        print("user_type : " + str(user_type) + ", type : " + str(type(user_type)))     

        try: 
            already_created_user = customUser.objects.get(username=row['username'])
            if update_existing_users:
                #Block of update
                continue
        except customUser.DoesNotExist:
            if create_users:
                #block of create
                new_user = customUser(
                            username = row['username'],
                            password = row['password'],
                            email    = row['email']
                            )
                new_user.save()


    """
    deleted      : 'Borrado',    #  Opcional
    suspended    : 'Suspendido',    #  Opcional
    username     : 'Usuario', # Puede que se use el de OAuth
    firstname    : 'Nombre',
    lastname     : 'Apellido',
    email        : 'Email',
    birthdate    : 'Cumpleaños',
    phonel       : 'Celular',
    phone2       : 'Telefono',
    institution  : 'Institucion',
    department   : 'Departamento',
    address      : 'Dirección',
    city         : 'Ciudad',

    firstlogin   : 'Primera Conexion',
    lastlogin    : 'Ultima Conexion',
    lastip       : 'Ultima IP',
    picture      : 'Imagen',
    description  : 'Descripcion',
    timecreated  : 'Creado',
    timemodified : 'Modificado',
    imagealt     : 'Imagen Alternativa',

    is_staff     : 'Staff',
    is_active    : 'Activo',
    is_superuser : 'SuperUsuario',
    last_login   : 'Ultima Conexion2',
    date_joined  : 'Fecha Creacion',
    
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1, label='Tipo de Usuario')







    """