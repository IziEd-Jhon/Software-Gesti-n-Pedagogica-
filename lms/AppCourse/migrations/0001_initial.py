# Generated by Django 4.0.4 on 2022-05-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=254)),
                ('shortname', models.CharField(max_length=100, unique=True)),
                ('summary', models.TextField(blank=True)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('visible', models.BooleanField(default=True)),
                ('timecreated', models.DateTimeField(auto_now_add=True)),
                ('timemodified', models.DateTimeField(auto_now=True)),
                ('grade', models.PositiveSmallIntegerField(choices=[(0, 'Custom'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=0)),
                ('grade_letter', models.CharField(default='', max_length=2)),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'Custom'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=0)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150)),
                ('description', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
    ]