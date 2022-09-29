# Generated by Django 4.0.5 on 2022-09-18 20:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0039_alter_emailconfirmationrequests_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationrequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 8, 20, 10, 718744, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='passwordchangerequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 8, 20, 10, 719255, tzinfo=utc)),
        ),
    ]
