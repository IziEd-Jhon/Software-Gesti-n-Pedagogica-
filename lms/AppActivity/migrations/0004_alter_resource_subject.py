# Generated by Django 4.0.4 on 2022-05-19 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCourse', '0009_section_correlative_alter_section_course_and_more'),
        ('AppActivity', '0003_assigment_resource_remove_activity_attempts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCourse.subject'),
        ),
    ]
