# Generated by Django 3.1 on 2020-09-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=200)),
                ('short_url', models.CharField(blank=True, max_length=6)),
            ],
        ),
    ]