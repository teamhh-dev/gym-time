# Generated by Django 3.1.2 on 2021-06-08 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0028_cashdet01_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdet01',
            name='party',
            field=models.ForeignKey(db_column='party', on_delete=django.db.models.deletion.CASCADE, to='gymapp.customer01'),
        ),
    ]
