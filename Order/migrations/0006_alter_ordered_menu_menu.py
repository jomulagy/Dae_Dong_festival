# Generated by Django 4.2.1 on 2023-05-15 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0004_remove_menu_mode_menu_mode'),
        ('Order', '0005_remove_order_menu_and_quantity_ordered_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.menu'),
        ),
    ]
