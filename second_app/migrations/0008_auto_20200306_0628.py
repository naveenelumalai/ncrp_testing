# Generated by Django 2.2.5 on 2020-03-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0007_auto_20200306_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ncrpcomplaints',
            name='AccusedPhoneNumber',
            field=models.CharField(max_length=264),
        ),
    ]
