# Generated by Django 4.0.5 on 2022-07-07 19:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_emailconfirmationrequests_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationrequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 8, 7, 18, 47, 455435, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='passwordchangerequests',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 8, 7, 18, 47, 456044, tzinfo=utc)),
        ),
    ]
