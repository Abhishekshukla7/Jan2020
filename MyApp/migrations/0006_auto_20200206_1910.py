# Generated by Django 3.0.2 on 2020-02-06 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_students_collega'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='Collega',
            new_name='College',
        ),
    ]
