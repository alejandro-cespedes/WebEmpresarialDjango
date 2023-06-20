from django.urls import path
from core.views import inicioPageView, AboutPageView, StorePageView

urlpatterns = [
    path("inicio/", inicioPageView.as_view(), name='inicio'),
    path("about/", AboutPageView.as_view(), name='about'),
    path("store/", StorePageView.as_view(), name='store'),
]