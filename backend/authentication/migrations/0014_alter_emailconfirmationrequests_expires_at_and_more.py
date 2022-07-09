# Generated by Django 4.0.5 on 2022-07-09 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_emailconfirmationrequests_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationrequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 10, 0, 17, 2, 850720, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='passwordchangerequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 10, 0, 17, 2, 851179, tzinfo=utc)),
        ),
    ]
