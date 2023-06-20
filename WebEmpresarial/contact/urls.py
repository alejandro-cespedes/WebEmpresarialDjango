from django.urls import path
import contact.views

urlpatterns = [
    path("", contact.views.contacto, name='contacto'),
]