# Generated by Django 4.2.2 on 2023-07-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0025_remove_usuario_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatares/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(blank=True, null=True, upload_to='media/imagenes/'),
        ),
    ]
