# Generated by Django 3.2 on 2021-04-25 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mypet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('reason', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True, max_length=250, null=True)),
                ('mail_alert', models.BooleanField()),
                ('pet_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypet.pet')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]