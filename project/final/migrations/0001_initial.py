# Generated by Django 4.0.3 on 2022-03-31 10:58

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.category', verbose_name='Категория')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Контент отклика')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика')),
                ('status_del', models.BooleanField(default=False, verbose_name='Статус отклика - отклонен')),
                ('status_add', models.BooleanField(default=False, verbose_name='Статус отклика - принят')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.note', verbose_name='Объявление')),
                ('user_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор отклика')),
            ],
        ),
    ]
