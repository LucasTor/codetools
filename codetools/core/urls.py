from django.urls import path
from codetools.core.views import home

urlpatterns = [
    path('', home),
]
