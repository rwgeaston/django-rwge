from django.urls import path
from django.conf import settings

from .views import rwge_view

urlpatterns = [
    path(settings.RWGE_URL, rwge_view),
]
