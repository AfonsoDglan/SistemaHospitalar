from atendimento.views import * 
from django.urls import path

app_name = 'atendimento'
urlpatterns = [
    path('triagem/', TriagemView.as_view(), name="triagem"),
    path('consulta/',ConsultaView.as_view(), name="consulta"),
    path('senha/', PedirSenhaView.as_view(), name="pedirSenha"),
    path('senhaconvencional/', SenhaConvencional.as_view(), name='senhaConvencional'),
    path('senhaprioritaria/', SenhaPrioritaria.as_view(), name="senhaPreferencial"),
    path('minhaSenha/', MinhaSenhaView.as_view(), name='minhaSenha')
]