# Generated by Django 2.2.5 on 2020-01-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20200124_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lab_batch',
            field=models.CharField(default='A1', max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='tut_batch',
            field=models.CharField(default='T1', max_length=2),
        ),
    ]
