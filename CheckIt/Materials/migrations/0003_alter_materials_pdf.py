# Generated by Django 3.2.4 on 2021-07-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Materials', '0002_materials_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='pdf',
            field=models.FileField(upload_to='File'),
        ),
    ]