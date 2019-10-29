# Generated by Django 2.2.1 on 2019-06-14 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('user_id', models.IntegerField(blank=True)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, verbose_name=datetime.datetime.now)),
            ],
        ),
    ]