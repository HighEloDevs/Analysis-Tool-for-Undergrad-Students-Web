# Generated by Django 4.0.5 on 2022-07-15 02:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0031_alter_emailconfirmationrequests_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationrequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 15, 14, 16, 59, 386335, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='passwordchangerequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 15, 14, 16, 59, 386836, tzinfo=utc)),
        ),
    ]
