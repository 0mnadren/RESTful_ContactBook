from django.urls import path
from . import views

app_name = 'contact_api'

urlpatterns = [
    path('', views.ContactAPIList.as_view(), name='contact_list'),
    path('<int:pk>/', views.ContactAPIDetail.as_view(), name='contact_detail'),
    path('birthday/', views.BirthdayAPIView.as_view(), name='birthday'),
]
