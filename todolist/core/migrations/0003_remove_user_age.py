# Generated by Django 4.1.6 on 2023-02-05 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
