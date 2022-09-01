from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class Email():
    @staticmethod
    def envio_html(url_context, context, parametros):
        context['urlsite'] = 'teste@gmail.com'
        html_content = render_to_string(url_context, context)

        ### INORAR O QUE VIR DE DOS PARAMETROS e CONCATENAR COM O NOME DO SISTEMA
        parametros['from_email'] = ''+parametros['from_email']+'<teste@gmail.com>'
        email = EmailMultiAlternatives(
                parametros['titulo'], 
                html_content,
                parametros['from_email'],                         
            )
        email.attach_alternative(html_content, "text/html")
       
        ### NO CASO DE NÃO SER INSERIDO O TO
        # UTIL NO CASO DE ENVIO PARA MULTIPLOS USUÁRIO COM BCC(oculto)        
        if 'to' in parametros:
            email.to = parametros['to']
        else:
            email.to = ['teste@gmail.com']

        if 'reply_to' in parametros:
            email.reply_to = parametros['reply_to']
        if 'cc' in parametros:
            email.cc = parametros['cc']
        if 'bcc' in parametros:
            email.bcc = parametros['bcc']
                
        if not 'bcc' in parametros and not 'to' in parametros:
            raise Exception("Você deve especificar o parâmetro TO, ou o BCC no caso de múltilpos envios")

        try:
            email.send(fail_silently=False)                
            print("SUCESSO envio_html")
            return True
        except Exception as e:
            print("############ERRO envio_html "+str(e))
            return e
