# Generated by Django 2.1.5 on 2019-09-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
