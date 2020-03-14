from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Service, Employee, Feature
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'core/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()[:6]
        context['employees'] = Employee.objects.all()
        #last top 3 features
        context['features_left'] = Feature.objects.order_by('-modified').all()[:3]
        #last top 4-6 features
        context['features_right'] = Feature.objects.order_by('-modified').all()[3:6]

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email successfully sent')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Fail sending email')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
