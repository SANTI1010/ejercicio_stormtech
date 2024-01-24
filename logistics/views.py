from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Paquete, ItemPlanilla

@api_view(['GET'])
def paquete_detail(request, tracking):
    try:
        paquete = Paquete.objects.get(tracking=tracking)
        item_planilla = ItemPlanilla.objects.filter(paquete=paquete).first()
        planilla = item_planilla.planilla if item_planilla else None

        data = {
            'paquete': {
                'tracking': paquete.tracking,
                'direccion_destinatario': paquete.direccion_destinatario,
                'telefono_destinatario': paquete.telefono_destinatario,
                'nombre_destinatario': paquete.nombre_destinatario,
                'peso': paquete.peso,
                'altura': paquete.altura,
                'estado': paquete.estado,
                'cliente': paquete.cliente.nombre,
                'tipo_paquete': paquete.tipo_paquete,
                'numero_planilla': planilla.numero_planilla if planilla else None,
                'fecha': planilla.fecha if planilla else None,
            }
        }

        return Response(data)
    except Paquete.DoesNotExist:
        return Response({'error': 'El paquete no existe'}, status=404)







