# Generated by Django 3.2.5 on 2021-10-16 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Materials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]