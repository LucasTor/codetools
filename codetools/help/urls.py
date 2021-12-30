from django.urls import path
from codetools.help.views import about

app_name = "about"

urlpatterns = [
    path('', about, name="about"),
]
