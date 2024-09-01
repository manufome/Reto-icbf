from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion
from .forms import PublicacionForm
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Actividad
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.is_administrador())
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    urls = {
        'crear': 'crear_publicacion',
        'editar': 'editar_publicacion',
        'eliminar': 'eliminar_publicacion',
    }
    objects = []
    for publicacion in publicaciones:
        objects.append({
            'Título': publicacion.titulo,
            'Descripción': publicacion.descripcion,
            'Fecha de Publicación': publicacion.fecha_publicacion,
            'Archivo': publicacion.archivo.name,
            'url_descargar': publicacion.archivo.url,
            'id': publicacion.pk
        })
    fields = ['Título', 'Descripción', 'Fecha de Publicación', 'Archivo']
    return render(request, 'crud/form_listar.html', {'objects': objects, 'urls': urls, 'title': 'Lista de Publicaciones', 'nuevo': 'Crear Nueva Publicación', 'fields': fields})


@login_required
@user_passes_test(lambda user: user.is_administrador())
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save()
            Actividad.objects.create(
                tipo='creacion',
                descripcion=f'Nueva publicación creada: "{publicacion.titulo}" el {publicacion.fecha_publicacion}',
                icono='fa-file-alt',
                content_type=ContentType.objects.get_for_model(publicacion),
                object_id=publicacion.id
            )
            messages.success(request, f'Publicación "{publicacion.titulo}" creada exitosamente el {publicacion.fecha_publicacion}')
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()

    return render(request, 'publicaciones/crear.html', {'form': form, 'title': 'Crear Publicación', 'back_url': 'lista_publicaciones'})


@login_required
@user_passes_test(lambda user: user.is_administrador())
def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            publicacion = form.save()
            cambios = form.changed_data
            Actividad.objects.create(
                tipo='edicion',
                descripcion=f'Publicación editada: "{publicacion.titulo}". Campos modificados: {", ".join(cambios)}',
                icono='fa-file-alt',
                content_type=ContentType.objects.get_for_model(publicacion),
                object_id=publicacion.id
            )
            messages.success(request, f'Publicación "{publicacion.titulo}" actualizada exitosamente. Campos modificados: {", ".join(cambios)}')
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm(instance=publicacion)

    return render(request, 'publicaciones/editar.html', {'form': form, 'title': 'Editar Publicación', 'back_url': 'lista_publicaciones'})


@login_required
@user_passes_test(lambda user: user.is_administrador())
def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        titulo = publicacion.titulo
        fecha = publicacion.fecha_publicacion
        archivo = publicacion.archivo
        Actividad.objects.create(
            tipo='eliminacion',
            descripcion=f'Publicación eliminada: "{titulo}" del {fecha}',
            icono='fa-file-alt',
            content_type=ContentType.objects.get_for_model(publicacion),
            object_id=publicacion.id
        )
        if archivo:
            import os
            from django.conf import settings
            ruta_archivo = os.path.join(settings.MEDIA_ROOT, str(archivo))
            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)
        publicacion.delete()
        messages.success(request, f'Publicación "{titulo}" del {fecha} eliminada exitosamente')
        return redirect('lista_publicaciones')

    return render(request, 'crud/form_eliminar.html', {'model': publicacion, 'title': 'Eliminar Publicación', 'back_url': 'lista_publicaciones'})
