# Generated by Django 2.1.5 on 2019-05-16 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
        ('blog', '0003_auto_20190516_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='channel.Channel'),
            preserve_default=False,
        ),
    ]
