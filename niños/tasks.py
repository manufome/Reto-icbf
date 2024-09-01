from background_task import background
from django.utils import timezone
from .models import Niño
from .utils import enviar_correo_cumpleaños,notificar_acudiente

@background(schedule=20)
def verificar_cumpleaños_diariamente():
    print("Verificando cumpleaños...")
    hoy = timezone.now().date()
    niños_cumpleaños = Niño.objects.filter(
        fecha_nacimiento__month=hoy.month,
        fecha_nacimiento__day=hoy.day
    )
    print(f"Niños con cumpleaños hoy: {niños_cumpleaños}")
    for niño in niños_cumpleaños:
        enviar_correo_cumpleaños(niño)
        if niño.get_edad() >= 5:
            notificar_acudiente(niño)
    

# python manage.py schedule_tasks