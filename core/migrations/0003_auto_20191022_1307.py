# Generated by Django 2.2.6 on 2019-10-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191022_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='learning',
            field=models.CharField(max_length=50, verbose_name='Learning'),
        ),
    ]
