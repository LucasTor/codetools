from django.urls import path
from codetools.lorem.views import lorem_ipsum, lorem_pixel, lorem_pixel_index

app_name = "lorem"

urlpatterns = [
    path('ipsum', lorem_ipsum, name="ipsum"),
    path('pixel', lorem_pixel, name="pixel"),
    path('pixel-index', lorem_pixel_index, name="pixel-index"),
]
