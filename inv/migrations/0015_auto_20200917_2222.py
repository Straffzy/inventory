# Generated by Django 3.1.1 on 2020-09-18 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0014_auto_20200917_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxes',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bx_wh', to='inv.warehouse'),
        ),
    ]
