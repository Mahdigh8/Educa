# Generated by Django 2.1.1 on 2018-09-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulecontinue',
            name='course',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='modulecontinue',
            name='module',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
