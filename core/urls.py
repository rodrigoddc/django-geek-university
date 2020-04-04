from django.urls import path
from .views import IndexView

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:lang_code_selected>/', IndexView.as_view(), name='language')
]
