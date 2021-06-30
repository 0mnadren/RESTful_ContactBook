from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={
            'input_type': 'password'
        },
        write_only=True
    )

    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if len(account.username) < 3:
            raise serializers.ValidationError({'username': 'Username must contain at least 3 characters.'})

        if len(password) < 6:
            raise serializers.ValidationError({'password': 'Password must be at least 6 characters long.'})

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            raise serializers.ValidationError('bad token.')


class AccountPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['pk', 'email', 'username']

