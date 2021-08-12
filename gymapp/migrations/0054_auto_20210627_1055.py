# Generated by Django 3.1.2 on 2021-06-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0053_auto_20210612_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='followup_date',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AlterField(
            model_name='member',
            name='end',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='start',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='dob',
            field=models.DateField(blank=True, default='2021-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='due_date',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='paid_date',
            field=models.DateField(default='2021-01-01'),
        ),
    ]
