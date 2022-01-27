# Generated by Django 4.0 on 2021-12-09 15:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Napitak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=30)),
                ('cijena', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(10)])),
                ('drzava', models.CharField(max_length=100)),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sladoled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=30)),
                ('datum_proizvodnje', models.DateField()),
                ('vegan', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sladoledni_kup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=30)),
                ('cijena', models.IntegerField(default=30, validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(30)])),
                ('opis', models.TextField()),
                ('sladoled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sladoled')),
            ],
        ),
    ]
