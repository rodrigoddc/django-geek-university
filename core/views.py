from django.views.generic import TemplateView, CreateView, ListView, DetailView


class IndexView(TemplateView):
    template_name = 'core/index.html'
