# Generated by Django 4.1.7 on 2023-03-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_resource_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(to='resources.resource'),
        ),
    ]
