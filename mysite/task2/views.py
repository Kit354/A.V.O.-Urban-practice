from django.views.generic import TemplateView
from django.shortcuts import render


def home(request):
    return render(request, 'func_template.html')


class class_templates(TemplateView):
    template_name = 'class_template.html'
