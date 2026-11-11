from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('', views.upload_form, name='upload-form'),
]

