# Generated by Django 3.2 on 2023-08-25 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elevaweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correo',
            name='email',
        ),
    ]
