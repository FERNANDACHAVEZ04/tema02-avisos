from django.urls import path
from .views import AvisosVigentesListView
from .views import landing_page

urlpatterns = [
    path('', AvisosVigentesListView.as_view(), name='lista_avisos'),
    path("",landing_page)
]


