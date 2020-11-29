# Generated by Django 3.0.3 on 2020-11-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportincidentmodel',
            name='reporting_user',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='date',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='immediate_action_taken',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='incident_department',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='incident_location',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='initial_severity',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='sub_incident_type',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='suspected_cause',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportincidentmodel',
            name='time',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
