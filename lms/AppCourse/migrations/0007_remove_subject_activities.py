# Generated by Django 4.0.4 on 2022-05-17 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCourse', '0006_alter_course_enddate_alter_course_shortname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='activities',
        ),
    ]