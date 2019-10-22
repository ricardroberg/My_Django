# Generated by Django 2.2.6 on 2019-10-22 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_by',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Learning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Last modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('learning', models.CharField(max_length=50, verbose_name='Knowledge')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('date_start', models.DateField(default=None, verbose_name='When start')),
                ('create_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Last modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('knowledge', models.CharField(max_length=50, verbose_name='Knowledge')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('create_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
