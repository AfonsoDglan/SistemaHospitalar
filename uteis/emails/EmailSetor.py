from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class Email():

    '''
        *url_context='emails/emailAlertaReserva.html'
        *context={'reserva': obj, 'listHistorico': historico}
    '''
    @staticmethod
    def envio_html(url_context, context, parametros):
        context['urlsite'] = 'palmas.uft.edu.br'
        html_content = render_to_string(url_context, context)

        email = EmailMultiAlternatives(
                parametros['titulo'], 
                html_content,
                parametros['from_email'], 
                parametros['to'],
                parametros['cc'],
            )
        # email = EmailMultiAlternatives(parametros['titulo'], html_content, parametros['from_email'], parametros['to'])
        email.attach_alternative(html_content, "text/html")
        # email.to = parametros['to']

        if parametros['reply_to']:
            email.reply_to = parametros['reply_to']


        
        # try:
        email.send(fail_silently=False)                
        # print("SUCESSO envio_html")
        # return True
        # except Exception as e:
        # print("ERRO envio_html"+str(e))
        # return e

'''
    obj = Reserva.objects.get(id=id)
    historico = HistoricoEvento.objects.filter(evento=obj.evento)[:5]
    context = {'reserva': obj, 'listHistorico': historico}
    
    html_content = render_to_string('emails/emailAlertaReserva.html', context)
    titulo = "[reservaweb] Alerta de Reserva de Recurso - "\
        +str(obj.espaco) + ' - '\
        +str(obj.data.strftime("%d/%m/%Y"))+' às '\
        +str(obj.horaInicio.strftime("%H:%M"))

    'email = EmailMultiAlternatives(titulo, html_content)
    'email.attach_alternative(html_content, "text/html")
    'email.to = ['reinaldotx@uft.edu.br']
    
    try:
        email.send(fail_silently=False)        
        # pass
    except Exception as e:
        print("ERRO NO EMAIL: " +str(e))

    # return render(request, 'emails/emailAlertaReserva.html', context)

    return HttpResponse('Hello, World!')
'''