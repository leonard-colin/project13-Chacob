# Generated by Django 3.2.16 on 2023-01-05 15:40

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mypet', '0007_alter_pet_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/2023-01-05'),
        ),
    ]
