# Generated by Django 3.0.3 on 2020-06-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todoDate',
            field=models.DateField(verbose_name='Due Date'),
        ),
    ]
