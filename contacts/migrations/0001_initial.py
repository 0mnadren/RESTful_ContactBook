# Generated by Django 3.2.4 on 2021-06-24 11:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55, verbose_name='first name')),
                ('last_name', models.CharField(max_length=55, verbose_name='last name')),
                ('nickname', models.CharField(blank=True, max_length=55)),
                ('company', models.CharField(blank=True, max_length=125)),
                ('job_title', models.CharField(blank=True, max_length=125, verbose_name='job title')),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(blank=True, max_length=125)),
                ('website', models.URLField(blank=True, max_length=225)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]