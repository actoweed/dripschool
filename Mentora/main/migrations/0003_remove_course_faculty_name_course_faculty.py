# Generated by Django 4.0.4 on 2024-11-24 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_course_faculty_course_faculty_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='faculty_name',
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.faculty'),
        ),
    ]
