from django.views.generic import ListView
from django.utils import timezone
from .models import Aviso
from django.shortcuts import render

# Función para la página de inicio
def landing_page(request):
    return render(request, "landing.html")

# Vista basada en clase para lista de avisos
class AvisosVigentesListView(ListView):
    model = Aviso
    template_name = "avisos/lista_avisos.html"
    context_object_name = "avisos"
    
    def get_queryset(self):
        hoy = timezone.now().date()
        return Aviso.objects.filter(
            fecha_inicio__lte=hoy,
            fecha_fin__gte=hoy
        ).order_by("-fecha_inicio")