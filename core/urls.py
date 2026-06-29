from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('hizmetler/', views.hizmetler, name='hizmetler'),
    path('projeler/', views.projeler, name='projeler'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('hizmet-detay/<slug:slug>/', views.hizmet_detay, name='hizmet_detay'),
    path('proje-detay/<slug:slug>/', views.proje_detay, name='proje_detay'),
]
