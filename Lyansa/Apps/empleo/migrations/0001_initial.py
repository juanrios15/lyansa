# Generated by Django 3.1.7 on 2021-02-28 19:03

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectos', '0008_auto_20210228_1209'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('resumen', ckeditor.fields.RichTextField(verbose_name='Resumen')),
                ('proyecto', models.CharField(max_length=250, verbose_name='Proyecto')),
                ('ubicacion', models.CharField(max_length=250, verbose_name='Ubicacion')),
                ('duracion', models.CharField(max_length=250, verbose_name='Duración')),
                ('salario', models.CharField(max_length=50, verbose_name='Salario')),
                ('publico', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('Categories', models.ManyToManyField(blank=True, related_name='empleos', to='proyectos.Categoria', verbose_name='Categorias')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Empleo',
                'verbose_name_plural': 'Empleos',
            },
        ),
    ]
