from django.urls import path
from codetools.lorem.views import lorem_ipsum

app_name = "lorem"

urlpatterns = [
    path('', lorem_ipsum, name="ipsum"),
]
