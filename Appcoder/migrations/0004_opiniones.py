# Generated by Django 5.0.6 on 2024-06-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0003_delete_cancionaaprender_delete_estudiante_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opiniones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=50)),
                ('sub', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=20)),
                ('cuerpo', models.CharField(max_length=500)),
            ],
        ),
    ]
