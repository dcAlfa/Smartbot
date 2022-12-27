# Generated by Django 3.2 on 2022-12-26 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=120, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hudud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default="Farg'ona", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shahar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default="Farg'ona", max_length=255)),
                ('hudud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smartapp.hudud')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, unique=True)),
                ('fulname', models.CharField(max_length=255)),
                ('lavozim', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=30)),
                ('shahar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smartapp.shahar')),
            ],
        ),
    ]