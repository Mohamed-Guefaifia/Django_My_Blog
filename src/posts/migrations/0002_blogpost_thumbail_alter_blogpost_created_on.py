# Generated by Django 4.2.7 on 2023-11-28 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
