# Generated by Django 2.2.5 on 2020-01-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0003_auto_20200108_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cyberstories',
            name='Published',
            field=models.DateField(),
        ),
    ]
