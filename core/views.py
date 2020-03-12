from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Service, Employee


class EmployeeList(ListView):
    template_name = 'core/team'
    model = Employee


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['employees'] = Employee.objects.all()

        return context
