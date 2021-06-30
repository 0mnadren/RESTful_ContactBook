from django.http import Http404
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegistrationSerializer, LogoutSerializer, AccountPropertiesSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from account.models import Account


class RegisterAPIView(APIView):

    def get(self, request):
        data = {
            'fields': {
                'email': 'Required field',
                'username': 'Required field',
                'password': 'Required field',
                'password2': 'Required field',
            }
        }
        return Response(data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data = {
                'success': 'Successfully registered a new user.',
                'email': account.email,
                'username': account.username,
            }

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountPropertiesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        try:
            account = request.user
            return account
        except Account.DoesNotExist:
            raise Http404

    def get(self, request):
        account = self.get_object(request)
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)


class UpdateAccountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        try:
            account = request.user
            return account
        except Account.DoesNotExist:
            raise Http404

    def put(self, request):
        account = self.get_object(request)
        serializer = AccountPropertiesSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Account update success.'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








