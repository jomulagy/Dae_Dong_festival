# Generated by Django 4.2.1 on 2023-05-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_rename_order_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(null=True, upload_to='menu'),
        ),
    ]
