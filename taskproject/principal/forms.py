from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Task


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name', 'email',]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'label']

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
        return task
