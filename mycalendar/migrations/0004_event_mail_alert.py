# Generated by Django 3.2 on 2021-04-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendar', '0003_alter_event_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='mail_alert',
            field=models.BooleanField(default=False),
        ),
    ]
