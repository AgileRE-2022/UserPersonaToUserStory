# Generated by Django 4.0.4 on 2022-07-07 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_userpersona_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersona',
            name='behaviours',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userpersona',
            name='frustrations',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userpersona',
            name='goals',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='userpersona',
            name='needs',
            field=models.TextField(max_length=1000),
        ),
    ]
