# Generated by Django 3.1.2 on 2021-06-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0020_auto_20210601_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='end',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='start',
            field=models.DateField(auto_now_add=True),
        ),
    ]
