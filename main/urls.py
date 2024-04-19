from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('shop/', shop, name="shop"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('test/', test, name="test"),
    path('processor/', process_data, name="processor"),
]

