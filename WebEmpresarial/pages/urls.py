from django.urls import path
import pages.views

urlpatterns = [
    path("<int:page_id>/<slug:page_slug>/", pages.views.page, name='page'),
]