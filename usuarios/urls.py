from django.urls import path
from .views import registro, login_view

urlpatterns = [
    path('registro/', registro),
    path('login/', login_view),
]