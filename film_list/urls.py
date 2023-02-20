from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_film/<str:pk>/', views.editFilm, name="edit_film"),
    path('delete/<str:pk>/', views.deleteFilm, name="delete"),
]
