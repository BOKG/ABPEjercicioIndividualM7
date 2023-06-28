from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView)

from .forms import TaskForm
from .models import Task


class Home(ListView):
    def get(self, request):
        return render(request, 'home.html', {})


class TaskListView(LoginRequiredMixin, ListView):

    model = Task
    template_name = 'pagina_principal.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        queryset = super().get_queryset()
        etiqueta = self.request.GET.get('etiqueta')
        estado = self.request.GET.get('estado')

        if etiqueta:
            queryset = queryset.filter(etiquetas__nombre=etiqueta)

        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset.order_by('due_date')


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'crear_tarea.html'
    success_url = reverse_lazy('pagina_principal')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Registro(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
