# Generated by Django 3.1.7 on 2021-03-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
