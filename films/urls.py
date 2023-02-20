
from django.contrib import admin
from django.urls import path, include
from film_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('film_list.urls'))
]
