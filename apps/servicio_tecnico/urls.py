from apps.servicio_tecnico.views import home, presupuesto, trabajos
from django.urls.conf import path


app_name = 'apps.servicio_tecnico'

urlpatterns = [
    path('', home, name='home'),
    path('api/trabajos',trabajos,name="trabajos"),
    path('servicio_tecnico/presupuesto',presupuesto,name="presupuesto"),
]