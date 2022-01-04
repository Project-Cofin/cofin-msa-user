# Generated by Django 4.0 on 2022-01-03 08:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_alter_message_msg_date_alter_message_msg_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_id',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(136000)]),
        ),
    ]