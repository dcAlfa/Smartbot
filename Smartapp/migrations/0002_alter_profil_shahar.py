# Generated by Django 3.2 on 2022-12-26 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Smartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='shahar',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='Smartapp.shahar'),
        ),
    ]