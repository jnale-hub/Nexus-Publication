from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("article/<str:id>", views.view_article, name="view_article"),
]
