# Generated by Django 4.0.5 on 2022-07-06 17:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_emailconfirmationrequests_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationrequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 7, 5, 2, 20, 778596, tzinfo=utc)),
        ),
    ]
