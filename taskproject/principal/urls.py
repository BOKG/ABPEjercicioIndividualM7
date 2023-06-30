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
    path('tarea/<int:pk>/', DetallesTarea.as_view(), name='tarea_detalles'),
    path('editar/<int:pk>/', EditTaskView.as_view(), name='editar_tarea'),
    path('complete/', CompleteTaskView.as_view(), name='complete_task'),
    path('tarea/<int:pk>/eliminar/', delete_task, name='eliminar_tarea'),

]
