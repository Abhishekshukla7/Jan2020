# Generated by Django 3.0.2 on 2020-02-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_students_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Teacher', models.CharField(max_length=100)),
                ('SubjectCode', models.IntegerField()),
            ],
        ),
    ]