# Generated by Django 3.1.2 on 2021-05-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0010_auto_20210531_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
