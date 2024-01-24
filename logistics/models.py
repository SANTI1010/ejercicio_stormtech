from django.db import models

class Cliente(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    tracking = models.CharField(max_length=100, unique=True)
    direccion_destinatario = models.CharField(max_length=200)
    telefono_destinatario = models.CharField(max_length=20)
    nombre_destinatario = models.CharField(max_length=100)
    peso = models.FloatField()
    altura = models.FloatField()
    ESTADO_CHOICES = [
        ('deposito', 'En deposito'),
        ('distribucion', 'En distribucion'),
    ]
    TIPO_PAQUETE_CHOICES = (
        ('P', 'Peso Menor 1000'),
        ('M', 'Peso Menor 3000'),
        ('G', 'Todo lo demas')
    )

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_paquete = models.CharField(max_length=20, choices=TIPO_PAQUETE_CHOICES)

    def __str__(self):
        return self.tracking + ' - ' + "Destinatario " + self.nombre_destinatario


class Planilla(models.Model):
    numero_planilla = models.CharField(max_length=100)
    fecha = models.DateField()
    items_planilla = models.ManyToManyField('ItemPlanilla',related_name='planilla_items')
    def __str__(self):
        return "Planilla nro " + self.numero_planilla
   
class ItemPlanilla(models.Model):
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE,related_name='planilla')
    posicion = models.PositiveIntegerField()
    motivo_fallo = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return "Planilla nro " + self.planilla.numero_planilla + " - Nombre Destinatario " + self.paquete.nombre_destinatario 

