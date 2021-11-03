from apps.servicio_tecnico.views import home, presupuesto, trabajos
from django.urls.conf import path
from django.urls.conf import re_path
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls.static import static

favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)


app_name = 'apps.servicio_tecnico'

urlpatterns = [
    path('', home, name='home'),
    path('api/trabajos',trabajos,name="trabajos"),
    path('servicio_tecnico/presupuesto',presupuesto,name="presupuesto"),
    #FavIcon    
    re_path(r'^favicon\.ico$', favicon_view),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)