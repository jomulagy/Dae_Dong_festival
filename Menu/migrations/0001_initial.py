# Generated by Django 4.2.1 on 2023-05-10 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='menu')),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('y', '주문가능'), ('n', '품절')], max_length=100)),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.order')),
            ],
        ),
    ]
