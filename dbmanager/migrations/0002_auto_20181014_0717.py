# Generated by Django 2.1.2 on 2018-10-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptionmedicine',
            name='composition',
            field=models.ManyToManyField(default=None, null=True, to='dbmanager.Composition'),
        ),
    ]
