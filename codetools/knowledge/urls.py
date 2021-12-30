from django.urls import path
from codetools.knowledge.views import apis

app_name = "knowledge"

urlpatterns = [
    path('', apis, name="apis"),
]
