from django.urls import path
from services.views import ServiceListView, ServiceDetailView ,ServiceCreate, ServiceUpdate, ServiceDelete

services_patterns = ([
    path("", ServiceListView.as_view(), name='services'),
    path("<int:pk>/", ServiceDetailView.as_view(), name='service'),
    path("create/", ServiceCreate.as_view(), name='create'),
    path("update/<int:pk>/", ServiceUpdate.as_view(), name='update'),
    path("delete/<int:pk>/", ServiceDelete.as_view(), name='delete'),
], 'services')

