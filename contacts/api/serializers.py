from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_account')
    email = serializers.SerializerMethodField('get_email_from_account')

    class Meta:
        model = Contact
        fields = ['first_name',
                  'last_name',
                  'nickname',
                  'email',
                  'birthday',
                  'company',
                  'job_title',
                  'phone_number',
                  'second_phone_number',
                  'address',
                  'website',
                  'username',
                  'active',
                  ]

    def get_username_from_account(self, contact):
        username = contact.account.username
        return username

    def get_email_from_account(self, contact):
        email = contact.account.email
        return email


