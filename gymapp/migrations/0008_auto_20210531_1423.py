# Generated by Django 3.1.2 on 2021-05-31 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0007_auto_20210531_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainee',
            old_name='pic',
            new_name='image',
        ),
    ]
