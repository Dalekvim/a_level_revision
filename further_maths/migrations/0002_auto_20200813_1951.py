# Generated by Django 3.1 on 2020-08-13 18:51

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('further_maths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proof',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
