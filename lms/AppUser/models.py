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
        username     = row.get(['username']).values[0]
        firstname    = None if 'firstname' not in row else row.get(['firstname']).values[0]
        lastname     = None if 'lastname' not in row else row.get(['lastname']).values[0]
        email        = row.get(['email']).values[0]
        birthdate    = None if 'birthdate' not in row else row.get(['birthdate']).values[0]
        phonel       = None if 'phonel' not in row else row.get(['phonel']).values[0]
        phone2       = None if 'phone2' not in row else row.get(['phone2']).values[0]
        institution  = None if 'institution' not in row else row.get(['institution']).values[0]
        department   = None if 'department' not in row else row.get(['department']).values[0]
        address      = None if 'address' not in row else row.get(['address']).values[0]
        city         = None if 'city' not in row else row.get(['city']).values[0]

        firstlogin   = None if 'firstlogin' not in row else row.get(['firstlogin']).values[0]
        lastlogin    = None if 'lastlogin' not in row else row.get(['lastlogin']).values[0]
        lastip       = None if 'lastip' not in row else row.get(['lastip']).values[0]
        picture      = None if 'picture' not in row else row.get(['picture']).values[0]
        description  = None if 'description' not in row else row.get(['description']).values[0]
        timecreated  = None if 'timecreated' not in row else row.get(['timecreated']).values[0]
        timemodified = None if 'timemodified' not in row else row.get(['timemodified']).values[0]
        imagealt     = None if 'imagealt' not in row else row.get(['imagealt']).values[0]

        is_staff     = False if 'is_staff' not in row else (
                        False if not DEBUGG_UPLOADFILE else (
                            False if row.get(['is_staff']).isnull().any() else (
                                Boolean(row.get(['is_staff']))
                            )))
        is_active   = True if 'is_active' not in row else (
                True if not DEBUGG_UPLOADFILE else (
                    True if row.get(['is_active']).isnull().any() else (
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
        last_login   = None if 'last_login' not in row else row.get(['last_login']).values[0]
        date_joined  = None if 'date_joined' not in row else row.get(['date_joined']).values[0]
        
        user_type    = row.get(['user_type'], default=customUser.UserTypeChoices.STUDENT)


       
        user_type = customUser.UserTypeChoices.STUDENT if 'user_type' not in row else (
                customUser.UserTypeChoices.STUDENT if row.get(['is_superuser']).isnull().any()
                    else int(row.get(['user_type']))
                )
        
        if int(user_type) == customUser.UserTypeChoices.ADMIN and not DEBUGG_UPLOADFILE:
            user_type = customUser.UserTypeChoices.CUSTOM

        """print("deleted : " + str(deleted) + ", type : " + str(type(deleted))) 
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
"""


        params = {
            "deleted" : deleted,
            "suspended" : suspended,
            "username" : username,
            "firstname" : firstname,
            "lastname" : lastname,
            "email" : email,
            "birthdate" : birthdate,
            "phonel" : phonel,
            "phone2" : phone2,
            "institution" : institution,
            "department" : department,
            "address" : address,
            "city" : city,
            "firstlogin" : firstlogin,
            "lastlogin" : lastlogin,
            "lastip" : lastip,
            "picture" : picture,
            "description" : description,
            "timecreated" : timecreated,
            "timemodified" : timemodified,
            "imagealt" : imagealt,
            "is_staff" : is_staff,
            "is_active" : is_active,
            "is_superuser" : is_superuser,
            "last_login" : last_login,
            "date_joined" : date_joined,
            "user_type" : user_type
        }
        not_none_params = {k:v for k, v in params.items() if v is not None and v is not NaN}

        print(str(params))
        print("********************************************")
        print("********************************************")
        print("********************************************")
        print(str(not_none_params))

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