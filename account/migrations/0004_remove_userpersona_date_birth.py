# Generated by Django 4.0.4 on 2022-07-06 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userpersona_behaviours_userpersona_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpersona',
            name='date_birth',
        ),
    ]
