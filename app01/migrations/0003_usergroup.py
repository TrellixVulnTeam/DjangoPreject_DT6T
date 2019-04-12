# Generated by Django 2.2 on 2019-04-11 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190411_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32, unique=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
