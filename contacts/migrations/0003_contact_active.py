# Generated by Django 3.2.4 on 2021-06-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_remove_contact_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]