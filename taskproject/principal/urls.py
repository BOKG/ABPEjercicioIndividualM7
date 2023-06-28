from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import *

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.Registro.as_view(), name='registro'),
    path('', TaskListView.as_view(), name='pagina_principal'),
    path('crear/', CreateTask.as_view(), name='crear_tarea'),
]
