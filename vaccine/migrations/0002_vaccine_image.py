# Generated by Django 5.0.3 on 2024-03-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vaccine_images/'),
        ),
    ]
