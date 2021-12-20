# Generated by Django 4.0 on 2021-12-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('msg_type', models.BooleanField()),
                ('msg_city', models.TextField()),
                ('msg_district', models.TextField()),
                ('msg_date', models.DateField()),
                ('msg_time', models.TimeField()),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]
