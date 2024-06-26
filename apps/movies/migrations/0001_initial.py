# Generated by Django 3.2.25 on 2024-04-22 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('minimum_age', models.IntegerField(verbose_name='Edad Minima')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=256, verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='movies', verbose_name='Imagen')),
                ('release_date', models.DateField(verbose_name='Fecha de publicacion')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.categories', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Pelicula',
                'verbose_name_plural': 'Peliculas',
            },
        ),
    ]
