# Generated by Django 3.1.2 on 2021-06-08 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0031_auto_20210608_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdet01',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.customer01'),
        ),
    ]
