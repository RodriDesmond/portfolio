from apps.servicio_tecnico.models import Jobs
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def trabajos(request):
    try:
        trabajo = Jobs.objects.all()
        trabajo = list(trabajo)
        data = []
        for t in trabajo:
            data.append({
                'categoria': t.categoria.nombre_categoria,
                'trabajo' : t.nombre,
                'precio' : t.valor,
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Algo malio sal")


def presupuesto(request):

    context = {
        'categoria': request.GET.get('categoria'),
        'trabajo' : request.GET.get('user_id'),
        'precio' : request.GET.get('puntaje'),
    }
    return render(request,'servicio_tecnico/presupuesto.html', context)