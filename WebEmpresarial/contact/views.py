from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contacto(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                f'De {name} <{email}>\n\nEscribio:\n\n{content}',
                'no-contestar@inbox.mailtrap.io',
                ["73208275@continental.edu.pe"],
                reply_to=[email]
            )
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contacto') + "?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contacto') + "?fail")

    return render(request, 'contact/contacto.html',{
        'form': contact_form
    })