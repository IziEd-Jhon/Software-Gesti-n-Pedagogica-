from tkinter import CASCADE
from turtle import title
from unicodedata import name
from django.db import InternalError, models

from AppCourse.models import Subject

class Resource(models.Model):
    title       = models.CharField(max_length=150, blank=False, default='')
    description = models.TextField(default='')
    timecreated = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    timemodified= models.DateTimeField(auto_now=True, null=True)
    subject     = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    activity    = models.ForeignKey('Activity', null=True, blank=True, on_delete=models.CASCADE)

    RESOURCE_TYPE_CHOICES = (
        (0, 'Custom'),
        (1, 'File'),
        (2, 'Folder'),
    )
    resource_type = models.PositiveSmallIntegerField(choices=RESOURCE_TYPE_CHOICES, default=0)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural="Recursos"

class Folder(Resource): 
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural="Archivos"

class Archive(Resource):
    file = models.FileField(upload_to='archives/')
    parent_folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural="Archivos"


class Activity(models.Model):
    title       = models.CharField(max_length=150, blank=False, default='')
    description = models.TextField(default='')
    subject     = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)
    timed_activity = models.BooleanField(default=False)
    timeopen	= models.DateTimeField(null=True, blank=True)
    timeclose	= models.DateTimeField(null=True, blank=True)
    timecreated = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    timemodified= models.DateTimeField(auto_now=True, null=True)

    ACTIVITY_TYPE_CHOICES = (
        (0, 'Custom'),
        (1, 'Quiz'),    # encuesta, cuestionario, quiz
        (2, 'Assigment'),
        (3, 'Forum'),
        (4, 'Lesson')
    )
    activity_type = models.PositiveSmallIntegerField(choices=ACTIVITY_TYPE_CHOICES, default=0)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural="Actividades"

class Quiz(Activity):
    gradeable   = models.BooleanField(default=False)
    max_grade   = models.FloatField(default=0.0, null=True, blank=True)
    timed_attempt  = models.BooleanField(default=False)
    timelimit   = models.BigIntegerField(default=0, null=True, blank=True)
    attempts    = models.SmallIntegerField(default=0, null=True, blank=True)

    GRADEMETHOD_TYPE_CHOICES = (
        (0, 'Custom'),
        (1, 'Automatic'), # lo hace el sistema en base a preguntas
        (2, 'Direct'),    # se pone la nota manual y directa
        (3, 'Rubric'),    # se hace en base a una rubrica por metas, cada meta con un puntaje asignado
        (4, 'Marking'),   # se hace rubrica pero cada rubrica se evalua en base a puntaje maximo
        (9, 'Mixed'),     # se convinan atomaticas y alguna de las otras 
    ) #https://medium.com/upeielo/grading-your-moodle-assignments-3-ways-c895a4a2d5ca#:~:text=In%20the%20Moodle%20assignment%20activity,%E2%80%9D%2C%20and%20%E2%80%9Crubric%E2%80%9D.
    grademethod_type = models.PositiveSmallIntegerField(choices=GRADEMETHOD_TYPE_CHOICES, default=0)

    decimalpoints           = models.SmallIntegerField(default=1, null=True, blank=True)
    questiondecimalpoints   = models.SmallIntegerField(default=1, null=True, blank=True)
    shuffleanswers          = models.BooleanField(default=False, null=True, blank=True)
    max_grade               = models.FloatField(default=7.0, null=True, blank=True)
    
    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quiz"
        
class Assigment(Activity):

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
