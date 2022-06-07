from email.policy import default
from pickle import FALSE
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin

from numpy import NaN
from pandas import DataFrame
from AppCourse.models import Course, Subject
from django.core.exceptions import MultipleObjectsReturned

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

    def save(self, *args, **kwargs):
        super(EnrollmentCourse, self).save(*args, **kwargs)
        subjects_of_course = list(Subject.objects.filter(course = self.course))
        for subject_of_course in subjects_of_course:
            if subject_of_course.auto_enroll:
                obj_enroll_sub, created_uos = EnrollmentSubject.objects.update_or_create(student = self.student,  subject = subject_of_course, defaults = 
                        {'status' : True})
                print(str(CustomEnrollmentSubjectSerializer(obj_enroll_sub).data))

DEBUGG_UPLOADFILE = True


from AppUser.serializer import CustomStudentSerializer, CustomEnrollmentCourseSerializer, CustomEnrollmentSubjectSerializer

def UploadUsersFromFile(reader: DataFrame, update_existing_users=True, create_users=True, enroll_courses=True, deactivate_enrolls=True):
    """
        update_existing_users en True hace que se actualizen los usuarios ya existentes,
        create_users en True hace que se creen los usuarios nuevos,
        combinando ambos se puede setear solo crear, solo updatear o ambos
    """

    if not update_existing_users and not create_users:
        return { 'error' : 'update_existing_users and create_users both false does nothing'}

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

    """results = {'successful': {
                    'created' : [],
                    'updated' : []
                },
                'failed' : {
                    'not updated' : [],
                    'not found' : []
                }}"""

    results ={  'users' : 
                    {'successful': {
                        'created' : [],
                        'updated' : []
                    },
                    'failed' : {
                        'not updated' : [],
                        'not found' : []
                    }},
                'course_enrollments' :
                    {'successful': {
                        'created' : [],
                        'updated' : []
                    },
                    'failed' : {
                        'not updated' : [],
                        'not found' : []
                    }},
                'subject_enrollments' :
                    {'successful': {
                        'created' : [],
                        'updated' : []
                    },
                    'failed' : {
                        'not updated' : [],
                        'not found' : []
                    }}
            }

    #from AppUser.serializer import CustomStudentSerializer

    for _, row in reader.iterrows():
        #block of reading values
        params = {
            'deleted'      : False if 'deleted' not in row else (
                            False if not DEBUGG_UPLOADFILE else (
                                False if row.get(['deleted']).isnull().any() else (
                                    Boolean(row.get(['deleted']))
                                ))),
            'suspended'      : False if 'suspended' not in row else (
                            False if not DEBUGG_UPLOADFILE else (
                                False if row.get(['suspended']).isnull().any() else (
                                    Boolean(row.get(['suspended']))
                                ))),                     
            'username'     : row.get(['username']).values[0],
            'password'     : row.get(['password']).values[0] if 'password' in row else (
                            row.get(['contraseña']).values[0]) if 'contraseña' in row else None,
            'firstname'    : None if 'firstname' not in row else row.get(['firstname']).values[0],
            'lastname'     : None if 'lastname' not in row else row.get(['lastname']).values[0],
            'email'        : row.get(['email']).values[0],
            'birthdate'    : None if 'birthdate' not in row else row.get(['birthdate']).values[0],
            'phonel'       : None if 'phonel' not in row else row.get(['phonel']).values[0],
            'phone2'       : None if 'phone2' not in row else row.get(['phone2']).values[0],
            'institution'  : None if 'institution' not in row else row.get(['institution']).values[0],
            'department'   : None if 'department' not in row else row.get(['department']).values[0],
            'address'      : None if 'address' not in row else row.get(['address']).values[0],
            'city'         : None if 'city' not in row else row.get(['city']).values[0],

            'firstlogin'   : None if 'firstlogin' not in row else row.get(['firstlogin']).values[0],
            'lastlogin'    : None if 'lastlogin' not in row else row.get(['lastlogin']).values[0],
            'lastip'       : None if 'lastip' not in row else row.get(['lastip']).values[0],
            'picture'      : None if 'picture' not in row else row.get(['picture']).values[0],
            'description'  : None if 'description' not in row else row.get(['description']).values[0],
            'timecreated'  : None if 'timecreated' not in row else row.get(['timecreated']).values[0],
            'timemodified' : None if 'timemodified' not in row else row.get(['timemodified']).values[0],
            'imagealt'     : None if 'imagealt' not in row else row.get(['imagealt']).values[0],

            'is_staff'     : False if 'is_staff' not in row else (
                            False if not DEBUGG_UPLOADFILE else (
                                False if row.get(['is_staff']).isnull().any() else (
                                    Boolean(row.get(['is_staff']))
                                ))),
            'is_active'   : True if 'is_active' not in row else (
                    True if not DEBUGG_UPLOADFILE else (
                        True if row.get(['is_active']).isnull().any() else (
                            Boolean(row.get(['is_active']))
                        ))),
            'is_superuser' : False if 'is_superuser' not in row else (
                    False if not DEBUGG_UPLOADFILE else (
                        False if row.get(['is_superuser']).isnull().any() else (
                            Boolean(row.get(['is_superuser']))
                        ))),
            'last_login'   : None if 'last_login' not in row else row.get(['last_login']).values[0],
            'date_joined'  : None if 'date_joined' not in row else row.get(['date_joined']).values[0],
            
            'user_type'    : row.get(['user_type'], default=customUser.UserTypeChoices.STUDENT),


        
            'user_type' : customUser.UserTypeChoices.STUDENT if 'user_type' not in row else (
                    customUser.UserTypeChoices.STUDENT if row.get(['is_superuser']).isnull().any() else (
                        customUser.UserTypeChoices.CUSTOM if int(row.get(['user_type'])) == customUser.UserTypeChoices.ADMIN and not DEBUGG_UPLOADFILE else (
                            int(row.get(['user_type']))
                        )))
        }

        course_to_enroll_id = str(row.get(['course']).values[0] if 'course' in row else (
                                row.get(['curso']).values[0] if 'curso' in row else None))

        not_none_params = {k:v for k, v in params.items() if v is not None and v is not NaN}

        if create_users:
                if update_existing_users:
                    obj_user, created_uoc = customUser.objects.update_or_create(username = not_none_params['username'], defaults = not_none_params)
                    if created_uoc:
                        results['users']['successful']['created'].append(CustomStudentSerializer(obj_user).data)
                    else:
                        results['users']['successful']['updated'].append(CustomStudentSerializer(obj_user).data)
              
                else:
                    obj_user, created_goc = customUser.objects.get_or_create(username = not_none_params['username'], defaults = not_none_params)
                    if created_goc:
                        results['users']['successful']['created'].append(CustomStudentSerializer(obj_user).data)
                    else:
                        results['users']['failed']['unchanged'].append(CustomStudentSerializer(obj_user).data)

                if params['password'] is not None:
                    obj_user.set_password(params['password'])
                    obj_user.save()  
   
        else:
            if update_existing_users:
                try: 
                    obj_user = customUser.objects.get(username = not_none_params['username'])
                    for k, v in not_none_params.items():
                        setattr(obj_user, k, v)
                    if params['password'] is not None:
                        obj_user.set_password(params['password'])
                        obj_user.save()
                    results['users']['successful']['updated'].append(CustomStudentSerializer(obj_user).data)
                except customUser.DoesNotExist:
                    results['users']['failed']['not found'].append({'username' : not_none_params['username']})

        if enroll_courses:
            if course_to_enroll_id is not None and course_to_enroll_id is not NaN and 'nan' not in course_to_enroll_id:
                try:
                    if course_to_enroll_id.isnumeric():
                        course_to_enroll = Course.objects.get(id=course_to_enroll_id)
                    else:
                        #f"{self.grade}{self.grade_letter}{self.get_level_display()[0]}{self.year}"
                        course_to_enroll = Course.objects.get(
                            grade=course_to_enroll_id[0], 
                            grade_letter=course_to_enroll_id[1],
                            level= 1 if 'B' in course_to_enroll_id[2] else (2 if 'M' in course_to_enroll_id[2] else 0),
                            year = course_to_enroll_id[-4:])
                   
                    if deactivate_enrolls:
                        already_enrolled_courses = list(EnrollmentCourse.objects.filter(student = obj_user))
                        for already_enrolled_course in already_enrolled_courses:
                            #print("user" + str(obj_user) + " already enrolled in " + str(already_enrolled_course))
                            if already_enrolled_course.status:
                                already_enrolled_course.status = False
                                already_enrolled_course.save()
                                results['course_enrollments']['successful']['updated'].append(CustomEnrollmentCourseSerializer(already_enrolled_course).data)

                    enroll_obj, created_enc = EnrollmentCourse.objects.update_or_create(student = obj_user, course=course_to_enroll, defaults = {
                        'status' : True
                    })

                    if created_enc:
                        results['course_enrollments']['successful']['created'].append(CustomEnrollmentCourseSerializer(enroll_obj).data)
                    else:
                        results['course_enrollments']['successful']['updated'].append(CustomEnrollmentCourseSerializer(enroll_obj).data)

                except (Course.DoesNotExist, MultipleObjectsReturned) as e:
                    if course_to_enroll_id.isnumeric():
                        results['users']['failed']['not found'].append({'id' : course_to_enroll_id})
                    else:
                        results['users']['failed']['not found'].append({'code' : course_to_enroll_id})

    return results