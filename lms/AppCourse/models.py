from django.db import models

from AppActivity.models import Activity

class Course(models.Model):
    fullname    = models.CharField(max_length=254, null=False, blank=False)
    shortname   = models.CharField(max_length=100, null=True, unique=True)
    summary     = models.TextField(blank=True)
    startdate   = models.DateTimeField(null=True)
    enddate     = models.DateTimeField(null=True)
    visible     = models.BooleanField(default=True)
    timecreated = models.DateTimeField(auto_now_add=True, editable=False)
    timemodified= models.DateTimeField(auto_now=True)

    COURSE_GRADE_CHOISES = (
        (0, 'Custom'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    )
    grade = models.PositiveSmallIntegerField(choices=COURSE_GRADE_CHOISES, default=0)
    grade_letter = models.CharField(max_length=2, default='')

    COURSE_LEVEL_CHOISES = (
        (0, 'Custom'),
        (1, 'Básico'),
        (2, 'Medio'),
    )
    level = models.PositiveSmallIntegerField(choices=COURSE_LEVEL_CHOISES, default=0)

    verbose = str(grade) + '° ' + str(grade_letter)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        
class Subject(models.Model):
    course  = models.OneToOneField(Course, null=True, blank=True, on_delete=models.CASCADE)
    title   = models.CharField(max_length=150, blank=False, default='')
    description = models.TextField(default='')

    activities  = models.ManyToManyField(Activity, blank=True)

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural="Materias"

#https://github.com/llazzaro/django-scheduler