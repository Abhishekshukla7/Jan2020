# Generated by Django 3.0.2 on 2020-02-26 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='ins',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MyApp.institute'),
        ),
    ]
