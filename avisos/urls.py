from django.urls import path
from .views import AvisosVigentesListView

urlpatterns = [
    path('', AvisosVigentesListView.as_view(), name='lista_avisos'),
]