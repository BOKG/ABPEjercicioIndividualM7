from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

from .forms import TaskForm, EditTaskForm
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
        return queryset.order_by('due_date')

    # show only task 'IP' or 'P'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = self.get_queryset().filter(status__in=['IP', 'P'])
        return context


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'crear_tarea.html'
    success_url = reverse_lazy('pagina_principal')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DetallesTarea(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tarea_detalles.html'
    context_object_name = 'tarea'
    fields = ['status']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea'] = self.get_queryset().first()
        return context

    def post(self, request, *args, **kwargs):
        tarea = self.get_queryset().first()
        tarea.status = request.POST.get('status')
        tarea.status = 'C'
        tarea.save()
        return redirect('pagina_principal')


class EditTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'editar_tarea.html'
    success_url = reverse_lazy('pagina_principal')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea'] = self.get_queryset().first()
        return context

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class CompleteTaskView(LoginRequiredMixin, ListView):

    model = Task
    template_name = 'tareas_completadas.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('due_date')
    # show only task 'IP' or 'P'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = self.get_queryset().filter(status__in=['C'])
        return context


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tareas/eliminar_tarea.html'
    context_object_name = 'tarea'
    success_url = reverse_lazy('tasks:lista')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


class Registro(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


def delete_task(request, pk):

    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('pagina_principal')
