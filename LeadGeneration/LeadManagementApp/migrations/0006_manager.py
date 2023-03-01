# Generated by Django 4.1.5 on 2023-01-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadManagementApp', '0005_cities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=45)),
                ('lastname', models.CharField(default='', max_length=45)),
                ('dob', models.DateField()),
                ('gender', models.CharField(default='', max_length=6)),
                ('emailid', models.CharField(default='', max_length=45)),
                ('mobileno', models.CharField(default='', max_length=12)),
                ('address', models.CharField(default='', max_length=200)),
                ('state', models.CharField(default='', max_length=45)),
                ('city', models.CharField(default='', max_length=45)),
                ('password', models.CharField(default='1234', max_length=50)),
                ('photograph', models.ImageField(upload_to='static/')),
            ],
        ),
    ]