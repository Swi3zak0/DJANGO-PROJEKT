# Generated by Django 5.0 on 2023-12-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_shoe_color_alter_shoe_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoecategory',
            name='url',
            field=models.URLField(default='/default-url/'),
        ),
    ]