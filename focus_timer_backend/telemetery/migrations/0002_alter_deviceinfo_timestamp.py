# Generated by Django 5.0.7 on 2024-07-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemetery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinfo',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
