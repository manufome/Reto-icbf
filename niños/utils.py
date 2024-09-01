from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def enviar_correo_cumpleaños(niño):
    asunto = f"¡Feliz cumpleaños a {niño.nombre}!"
    contexto = {
        'nombre_niño': niño.nombre,
        'nombre_acudiente': niño.acudiente.first_name,
    }
    html_mensaje = render_to_string('emails/feliz_cumpleaños.html', contexto)
    mensaje_plano = strip_tags(html_mensaje)
    try:
        send_mail(
            asunto,
            mensaje_plano,
            settings.EMAIL_HOST_USER,
            [niño.acudiente.email],
            html_message=html_mensaje,
            fail_silently=False,
        )
        print("Correo enviado con éxito")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def notificar_acudiente(niño):
    asunto = f"Alerta: {niño.nombre} cumplirá 6 años el próximo año"
    mensaje = f"El niño {niño.nombre} cumplirá 6 años el próximo año. Por favor, prepare los documentos necesarios para su traslado a un colegio."
    try:
        send_mail(
            asunto,
            mensaje,
            settings.EMAIL_HOST_USER,
            [niño.acudiente.email],
            fail_silently=False,
        )
        print(f"Notificación enviada al jardín de {niño.nombre}")
    except Exception as e:
        print(f"Error al enviar la notificación: {e}")
