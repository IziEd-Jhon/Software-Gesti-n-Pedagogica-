# Generated by Django 4.0.4 on 2022-05-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCourse', '0009_section_correlative_alter_section_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='startdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
