from django.shortcuts import render

from app.forms import *
from django.http import HttpResponse
from django.views.generic import FormView
# Create your views here.

class Student_form (FormView):
    template_name='student_form.html'
    form_class=student

    def form_valid(self, form):
        form.save()
        return HttpResponse('insert_data_SuryaGFList is done successfully')