# Generated by Django 3.1 on 2020-08-13 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('further_maths', '0002_auto_20200813_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proof',
            name='title',
        ),
    ]
