# Generated by Django 3.1.2 on 2021-06-01 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0017_auto_20210601_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateField(blank=True, default='dd/mm/yyyy'),
        ),
        migrations.AlterField(
            model_name='member',
            name='package',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='gymapp.packages'),
        ),
        migrations.AlterField(
            model_name='member',
            name='whatsapp',
            field=models.CharField(default=0, max_length=100),
        ),
    ]