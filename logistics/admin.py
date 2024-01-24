from django.contrib import admin
from .models import Paquete, Planilla, ItemPlanilla, Cliente
from django.contrib import messages


@admin.action(description="Pasar a distribucion")
def pasar_a_distribucion(modeladmin, request, queryset):
    # Obtengo el nro de planilla
    for planilla in queryset:
        item = ItemPlanilla.objects.filter(planilla_id=planilla.id)
        for item in queryset:
            paquetes = Paquete.objects.filter(id=item.id)
            print(paquetes)
            for paquete in paquetes:
                paquete.estado = 'distribucion'
                paquete.save()

    messages.success(request, "La accion se ha actualizado correctamente.")


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