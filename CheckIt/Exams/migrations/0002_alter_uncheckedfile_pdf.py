# Generated by Django 3.2.4 on 2021-07-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uncheckedfile',
            name='pdf',
            field=models.FileField(upload_to='files'),
        ),
    ]
