# Generated by Django 4.0.4 on 2022-05-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppActivity', '0001_initial'),
        ('AppCourse', '0002_subject_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='activities',
            field=models.ManyToManyField(blank=True, null=True, to='AppActivity.activity'),
        ),
    ]