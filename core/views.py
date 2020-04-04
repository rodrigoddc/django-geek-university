from django.contrib import messages
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Service, Employee, Feature
from .forms import ContactForm
from django.utils.translation import gettext as _
from django.utils import translation


class IndexView(FormView):
    template_name = 'core/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        """
        Override get_context_data() to return:
        top 6 Services
        top 6 Employee
        top 6 Features (2 querysets with 3 eachone)
        Internalization translate if selected
        """
        context = super(IndexView, self).get_context_data(**kwargs)

        context['services'] = Service.objects.order_by('?').all()[:6]
        context['employees'] = Employee.objects.all()[:6]

        # last top 3 features
        context['features_left'] = Feature.objects.order_by('-modified').all()[:3]

        # last top 4-6 features
        context['features_right'] = Feature.objects.order_by('-modified').all()[3:6]
        context['available_languages'] = ['en', 'pt-br']

        # get language from browser request
        lang_browser = self.request.LANGUAGE_CODE

        # get language code if selected
        lang_code_selected = context['view'].kwargs.get('lang_code_selected', None)

        if lang_code_selected:
            translation.activate(lang_code_selected)

            # set lang_browser value to template tag html in attribute lang=""
            context['lang_browser'] = lang_code_selected

        else:
            translation.activate(lang_browser)

            # set lang_browser value to template tag html in attribute lang=""
            context['lang_browser'] = lang_browser

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('Email successfully sent'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Fail sending email'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
