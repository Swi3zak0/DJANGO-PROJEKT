# Generated by Django 5.0 on 2023-12-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produkt',
            old_name='typ',
            new_name='kategoria',
        ),
        migrations.AddField(
            model_name='produkt',
            name='kolor',
            field=models.CharField(default='czarny', max_length=16),
        ),
    ]
