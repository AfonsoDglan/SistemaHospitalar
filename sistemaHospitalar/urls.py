from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url, include
from django.urls import path, include

###
from django.conf import settings
from django.conf.urls.static import static

###
from atendimento.views.index import IndexView
from atendimento.views.autenticacao.login import LoginView

urlpatterns = [
    # LOGIN / LOGOUT 
    path('', IndexView.as_view(), name="index"),     
    path('p/login', LoginView.as_view(), name='login'),    
    #path('p/logout', , name='logout'),  
     # ADMIN    
    path('admin/', admin.site.urls),
    ###
    path('atendimento/', include('atendimento.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)