# Generated by Django 3.0.2 on 2020-01-30 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
    ]