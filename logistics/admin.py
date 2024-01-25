from django.contrib import admin
from .models import Paquete, Planilla, ItemPlanilla, Cliente
from django.contrib import messages
from django.db import transaction

@admin.action(description="Pasar a distribucion")
def pasar_a_distribucion(modeladmin, request, queryset):
    try:
        with transaction.atomic():
            for planilla in queryset:
                items = ItemPlanilla.objects.filter(planilla_id=planilla.id).select_related('paquete')
                for item in items:
                    Paquete.objects.filter(id=item.paquete_id).update(estado='distribucion')

            messages.success(request, "La accion se ha actualizado correctamente.")
    except Exception as e:
        messages.error(request, f"Error al realizar la accion: {str(e)}")



class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

class PaqueteAdmin(admin.ModelAdmin):
    list_filter = ('estado', 'cliente', 'tipo_paquete')
    search_fields = ('tracking', 'direccion_destinatario', 'nombre_destinatario')

class PlanillaAdmin(admin.ModelAdmin):
    actions = [pasar_a_distribucion]
    search_fields = ('numero_planilla',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(Planilla, PlanillaAdmin)
admin.site.register(ItemPlanilla)