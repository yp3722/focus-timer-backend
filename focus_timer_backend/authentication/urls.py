from django.urls import path
from .views import exchange_token

urlpatterns = [
    path('authentication/exchange-token/<str:backend>/', exchange_token, name='exchange-token'),
]