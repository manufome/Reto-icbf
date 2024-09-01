from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from niños.models import Asistencia, Niño
from jardines.models import Jardin
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

@login_required
@user_passes_test(lambda user: user.is_administrador())
def reportes_general(request):
    # Aquí obtenemos los datos para todos los reportes
    fecha_fin = timezone.now().date()
    # Ajustamos la fecha de inicio para excluir sábados y domingos
    fecha_inicio = fecha_fin - timedelta(days=fecha_fin.weekday())
    if fecha_inicio > fecha_fin:
        fecha_inicio -= timedelta(days=7)
    
    # Obtenemos solo los jardines aprobados
    jardines_aprobados = Jardin.get_aprobados()
    
    # Datos para reporte_semanal_asistencia
    asistencias = Asistencia.objects.filter(
        fecha__range=[fecha_inicio, fecha_fin], 
        fecha__week_day__range=[2, 6],
        niño__jardin__in=jardines_aprobados
    )
    
    reporte_asistencia = {}
    for jardin in jardines_aprobados:
        asistencias_jardin = asistencias.filter(niño__jardin=jardin)
        total_asistencias = asistencias_jardin.values('fecha').distinct().count()
        
        # Obtener todos los niños del jardín
        niños = Niño.objects.filter(jardin=jardin)
        
        asistencias_por_niño = {}
        for niño in niños:
            nombre = niño.nombre + ' ' + niño.acudiente.last_name
            asistencias_semana = []
            for dia in range(5):  # Solo de lunes a viernes
                fecha = fecha_inicio + timedelta(days=dia)
                asistencia = asistencias_jardin.filter(niño=niño, fecha=fecha).first()
                if asistencia:
                    asistencias_semana.append(asistencia.estado_nino)
                else:
                    asistencias_semana.append('No registrado')
            asistencias_por_niño[nombre] = asistencias_semana
        
        reporte_asistencia[jardin.nombre] = {
            'total_asistencias': total_asistencias,
            'asistencias_por_niño': asistencias_por_niño
        }

    # Datos para reporte_inasistencias_enfermedad
    inasistencias = Asistencia.objects.filter(
        fecha__range=[fecha_inicio, fecha_fin],
        fecha__week_day__range=[2, 6],
        estado_nino='Enfermo',
        niño__jardin__in=jardines_aprobados
    ).values('niño__jardin__nombre').annotate(total=Count('id'))
    
    # Datos para reporte_niños_por_jardin
    jardines_con_niños = jardines_aprobados.annotate(total_niños=Count('niños'))
    
    # Datos para reporte_jardines_no_aprobados
    jardines_no_aprobados = Jardin.objects.filter(estado__in=['En trámite', 'Negado'])
    
    hay_jardines_no_aprobados = jardines_no_aprobados.exists()
    
    context = {
        'reporte': reporte_asistencia,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'inasistencias': inasistencias,
        'jardines': jardines_con_niños,
        'jardines_no_aprobados': jardines_no_aprobados,
        'hay_jardines_no_aprobados': hay_jardines_no_aprobados,
    }
    return render(request, 'reportes/reportes_general.html', context)