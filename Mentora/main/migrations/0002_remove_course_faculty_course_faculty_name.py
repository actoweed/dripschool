# Generated by Django 4.0.4 on 2024-11-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='faculty',
        ),
        migrations.AddField(
            model_name='course',
            name='faculty_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
