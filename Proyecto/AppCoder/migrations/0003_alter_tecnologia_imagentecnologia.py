# Generated by Django 4.2.1 on 2023-06-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alter_tecnologia_imagentecnologia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnologia',
            name='imagenTecnologia',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
