# Generated by Django 3.1.2 on 2021-06-08 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0029_auto_20210608_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdet01',
            name='party',
            field=models.ForeignKey(db_column='id_party', on_delete=django.db.models.deletion.CASCADE, to='gymapp.customer01'),
        ),
    ]