from django.urls import path
from codetools.knowledge.views import apis, open_source_tools

app_name = "knowledge"

urlpatterns = [
    path('apis', apis, name="apis"),
    path('open-source-tools', open_source_tools, name="open-source-tools"),
]
