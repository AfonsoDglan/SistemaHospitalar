from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url, include
from django.urls import path, include

###
from django.conf import settings
from django.conf.urls.static import static

###
from atendimento.views import LoginViews as viewLogin
from atendimento.views import SelecionaModuloTemplateView

urlpatterns = [
    # LOGIN / LOGOUT 
    path('', SelecionaModuloTemplateView.as_view(), name="indexSistema"),     
    path('p/login', viewLogin.newlogin, name='login'),    
    path('p/logout', viewLogin.newlogout, name='logout'),  
     # ADMIN    
    path('admin/', admin.site.urls),
    ###
    path('atendimento/', include('atendimento.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)