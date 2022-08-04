# Generated by Django 3.2.4 on 2021-08-03 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100, verbose_name='Название локации/n')),
                ('description', models.CharField(max_length=5000, verbose_name='Описание локации')),
                ('city', models.CharField(max_length=100, verbose_name='Город (Ближайший город')),
                ('way', models.CharField(max_length=5000, verbose_name='Как добраться (детали проезда/прохода до места)')),
                ('img', models.ImageField(upload_to='', verbose_name='Фото локации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
