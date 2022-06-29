from asyncio.windows_events import NULL
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
import datetime

from AppUser.models import customUser

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

    level = models.PositiveSmallIntegerField(choices=CourseLevelChoises.choices, default=CourseLevelChoises.CUSTOM, verbose_name='Nivel')

    year = models.PositiveIntegerField(null=True, blank=False, verbose_name='Año', default=datetime.datetime.now().year,
        validators=[MinValueValidator(2000), MaxValueValidator(2050)])

    class_teacher = models.ForeignKey('AppUser.customUser', on_delete=models.CASCADE, blank=True, null=True, limit_choices_to={'user_type':customUser.UserTypeChoices.TEACHER})

    class Meta:
        unique_together = [['grade', 'grade_letter', 'level', 'year']]
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.verbose
        
class Subject(models.Model):
    course  = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Curso')
    title   = models.CharField(max_length=150, blank=False, default='', verbose_name='Titulo')
    auto_enroll = models.BooleanField(default=True, verbose_name='Matricula Automatica')
    description = models.TextField(default='', blank=True, null=True, verbose_name='Descripccion')

    subject_teacher = models.ForeignKey('AppUser.customUser', on_delete=models.CASCADE, blank=True, null=True, limit_choices_to={'user_type':customUser.UserTypeChoices.TEACHER})
     
    class Meta:
        verbose_name = "Materia"
        verbose_name_plural="Materias"

    def __str__(self):
        return str(self.course) + "-" + self.title

class Section(models.Model):
    subject  = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    correlative = models.SmallIntegerField(default=0, null=True, blank=True)
    title = models.CharField(max_length=150, blank=False, default='')
    description = models.TextField(default='')

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural="Secciones"

#https://github.com/llazzaro/django-scheduler