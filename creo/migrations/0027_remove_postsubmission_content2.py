# Generated by Django 2.1.2 on 2019-01-03 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0026_postsubmission_content2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postsubmission',
            name='content2',
        ),
    ]
