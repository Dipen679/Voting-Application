
from django.contrib import admin
from django.urls import path , include
from auapp.views import uhome,usignup,ulogout,ucp,ucreate,uvote,uresult,uhome1,remques

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",uhome,name="uhome"),
    path("usignup",usignup,name="usignup"),
    path("ulogout",ulogout,name="ulogout"),
    path("ucp",ucp,name="ucp"),	
    path("ucreate/",ucreate,name="ucreate"),
    path('uvote/<poll_id>/',uvote,name='uvote'),
    path('uresult/<poll_id>/',uresult,name='uresult'),
    path("uhome1",uhome1,name="uhome1"),
    path("remques/<poll_id>/",remques,name="remques"),
    path('admin/', admin.site.urls),
    
]
