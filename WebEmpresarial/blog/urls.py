from django.urls import path
import blog.views

urlpatterns = [
    path("", blog.views.blog, name='blog'),
    path("category/<int:category_id>", blog.views.category, name='category'),
]