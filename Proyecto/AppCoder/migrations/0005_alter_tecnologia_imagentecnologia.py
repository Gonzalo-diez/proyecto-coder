# Generated by Django 4.2.1 on 2023-06-21 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_alter_tecnologia_imagentecnologia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnologia',
            name='imagenTecnologia',
            field=models.ImageField(blank=True, null=True, upload_to='Proyecto\\AppCoder\\static\\AppCoder\\img'),
        ),
    ]