from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .serializers import ContactSerializer
from contacts.models import Contact
from rest_framework.permissions import IsAuthenticated
from django.db.utils import IntegrityError
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter


class ContactAPIList(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):

    serializer_class = ContactSerializer
    queryset = Contact.objects.filter(active=True)
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name',
                     'last_name',
                     'nickname',
                     'job_title',
                     'address',
                     )

    def get(self, request):
        return self.list(request)

    def post(self, request):
        try:
            account = request.user

            contact = Contact(account=account)

            serializer = ContactSerializer(contact, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'response': 'You have already created a contact.'})


class ContactAPIDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        contact = self.get_object(pk)

        user = request.user
        if contact.account != user:
            return Response({'response': "You don't have permission to edit that."})

        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_object(pk)

        user = request.user
        if contact.account != user:
            return Response({'response': "You don't have permission to delete that."})

        serializer = ContactSerializer(contact, data={'active': False}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BirthdayAPIView(APIView):
    """
    To add query parameters you must use browser's url or some app like Postman
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.query_params.get('is_older_than'):
            is_older_than = request.query_params.get('is_older_than')

            contacts = Contact.objects.filter(birthday__lt=is_older_than)
            serializer = ContactSerializer(contacts, many=True)

            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
