# Generated by Django 4.0 on 2022-01-03 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg_time',
            field=models.TextField(),
        ),
    ]
