from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['Tasks']
		fields = "__all__"