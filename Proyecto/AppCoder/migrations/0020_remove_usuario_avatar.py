# Generated by Django 4.2.2 on 2023-07-01 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0019_usuario_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='avatar',
        ),
    ]
