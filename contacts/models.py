from django.db import models
from django.core.validators import RegexValidator
from account.models import Account


class Contact(models.Model):
    first_name = models.CharField(verbose_name='first name', max_length=55)
    last_name = models.CharField(verbose_name='last name', max_length=55)
    nickname = models.CharField(max_length=55, blank=True)
    company = models.CharField(max_length=125, blank=True)
    job_title = models.CharField(verbose_name='job title', max_length=125, blank=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    second_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    address = models.CharField(max_length=125, blank=True)
    birthday = models.DateField(null=True, blank=True)
    website = models.URLField(max_length=225, blank=True)
    active = models.BooleanField(default=True, blank=True)

    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

