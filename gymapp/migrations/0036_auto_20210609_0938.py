# Generated by Django 3.1.2 on 2021-06-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0035_auto_20210609_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdet01',
            name='entrydate',
            field=models.DateTimeField(default='yyyy-mm-dd'),
        ),
    ]
