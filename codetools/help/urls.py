from django.urls import path
from codetools.help.views import about, contrib

app_name = "about"

urlpatterns = [
    path('', about, name="about"),
    path('contribuir', contrib, name="contrib"),
]
