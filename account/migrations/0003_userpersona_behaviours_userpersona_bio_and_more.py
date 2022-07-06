# Generated by Django 4.0.4 on 2022-07-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userpersona_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpersona',
            name='behaviours',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userpersona',
            name='bio',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='userpersona',
            name='date_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userpersona',
            name='frustrations',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userpersona',
            name='locations',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
