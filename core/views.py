from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Service, Employee, Feature


class EmployeeList(ListView):
    template_name = 'core/team'
    model = Employee


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()[:6]
        context['employees'] = Employee.objects.all()
        #last top 3 features
        context['features_left'] = Feature.objects.order_by('-modified').all()[:3]
        #last top 4-6 features
        context['features_right'] = Feature.objects.order_by('-modified').all()[3:6]



        return context
