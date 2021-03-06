# Generated by Django 3.1.1 on 2020-09-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0003_auto_20200906_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxes',
            name='box_name',
            field=models.CharField(default='box', max_length=20),
        ),
        migrations.AddField(
            model_name='items',
            name='item_name',
            field=models.CharField(default='name', max_length=50),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='warehouse_name',
            field=models.CharField(default='warehouse', max_length=100),
        ),
    ]
