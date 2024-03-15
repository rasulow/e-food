# Generated by Django 5.0.3 on 2024-03-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_brand_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='name_tm',
        ),
        migrations.AddField(
            model_name='brand',
            name='name',
            field=models.CharField(default='brand', max_length=100, verbose_name='Name'),
        ),
    ]