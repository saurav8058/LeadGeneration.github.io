# Generated by Django 4.1.5 on 2023-01-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadManagementApp', '0002_alter_employee_photograph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photograph',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
