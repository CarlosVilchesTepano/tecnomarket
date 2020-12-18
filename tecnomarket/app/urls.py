from django.urls import path
from .views import home, contacto, galeria

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('contacto/', contacto, name="contacto"),
]