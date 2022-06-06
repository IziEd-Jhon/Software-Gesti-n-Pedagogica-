from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
import datetime

class Course(models.Model):
    
    @property
    def verbose(self):
        """composite name of grade and letter"""
        return f"{self.grade}° {self.get_level_display()} {self.grade_letter} - {self.year}"

    @property
    def code(self):
        """composite identifying code 7 alphanumeric values, meaning: {grade}{letter}{level(B/M)}{year}"""
        return f"{self.grade}{self.grade_letter}{self.get_level_display()[0]}{self.year}"

    #fullname    = models.CharField(max_length=254, null=False, blank=False, verbose_name='Nombre Completo')
    #shortname   = models.CharField(max_length=100, null=True, unique=True, verbose_name='Nombre Corto')
    summary     = models.TextField(null=True, blank=True, verbose_name='Resumen')
    #startdate   = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Inicio')
    #enddate     = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Termino')
    visible     = models.BooleanField(default=True, verbose_name='Visibilidad')
    timecreated = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    timemodified= models.DateTimeField(auto_now=True, null=True)

    class CourseGradeChoises(models.IntegerChoices):
        CUSTOM = 0, 'Custom'
        PRIMERO = 1, 'Primero'
        SEGUNDO = 2, 'Segundo'
        TERCERO = 3, 'Tercero'
        CUARTO  = 4, 'Cuardo'
        QUINTO  = 5, 'Quinto'
        SEXTO   = 6, 'Sexto'
        SEPTIMO = 7, 'Séptimo'
        OCTAVO  = 8, 'Octavo'

    grade = models.PositiveSmallIntegerField(choices=CourseGradeChoises.choices, default=CourseGradeChoises.CUSTOM, verbose_name='Grado')
    
    alpha = RegexValidator(r'^[A-Z]*$', 'Only capitalized alpha characters are allowed.')
    grade_letter = models.CharField(max_length=2, default='', verbose_name='Letra', validators=[alpha])

    class CourseLevelChoises(models.IntegerChoices):
        CUSTOM  = 0, 'Custom'
        BASICO = 1, 'Básico'
        MEDIO = 2, 'Medio'

    level = models.PositiveSmallIntegerField(choices=CourseLevelChoises.choices, default=CourseLevelChoises.CUSTOM, verbose_name='Tipo de Usuario')

    year = models.PositiveIntegerField(null=True, blank=False, verbose_name='Año', default=datetime.datetime.now().year,
        validators=[MinValueValidator(2000), MaxValueValidator(2050)])

    class Meta:
        unique_together = [['grade', 'grade_letter', 'level', 'year']]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    
    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)
        print(self.timecreated)
        
class Subject(models.Model):
    course  = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Curso')
    title   = models.CharField(max_length=150, blank=False, default='', verbose_name='Titulo')
    auto_enroll = models.BooleanField(default=True, verbose_name='Matricula Automatica')
    description = models.TextField(default='', blank=True, null=True, verbose_name='Descripccion')

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural="Materias"

class Section(models.Model):
    subject  = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    correlative = models.SmallIntegerField(default=0, null=True, blank=True)
    title = models.CharField(max_length=150, blank=False, default='')
    description = models.TextField(default='')

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural="Secciones"

#https://github.com/llazzaro/django-scheduler
""">>> subjects = AppCourse.models.Subject.objects.all()
>>> print(vars(subjects[0]))
{'_state': <django.db.models.base.ModelState object at 0x0000025CDA1E9D80>, 'id': 1, 'course_id': 1, 'title': 'Leng auto', 'auto_enroll': True, 'description': 'punk'}
>>> subjectsofcourse = AppCourse.models.Subject.objects.filter(course_id=curso_id)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'curso_id' is not defined
>>> subjectsofcourse = AppCourse.models.Subject.objects.filter(course_id=curso.id)
>>> print(str(subjectsofcourse))
<QuerySet [<Subject: Subject object (1)>, <Subject: Subject object (2)>, <Subject: Subject object (3)>]>
>>> subjectsofcourse = AppCourse.models.Subject.objects.filter(course_id=curso.id, auto_enroll=True)
>>> print(str(subjectsofcourse))
<QuerySet [<Subject: Subject object (1)>, <Subject: Subject object (2)>]>
>>>"""