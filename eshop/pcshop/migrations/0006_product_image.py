# Generated by Django 3.1 on 2020-08-22 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcshop', '0005_auto_20200822_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
