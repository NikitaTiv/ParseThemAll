from django.urls import path

from images.views import upload_image

app_name = 'images'
urlpatterns = [
    path('', upload_image, name='image_main'),
]
