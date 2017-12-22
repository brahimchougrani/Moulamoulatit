from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^supprimer/(?P<pk>\d+)/$', views.Circuitdelete.as_view(), name="Circuitdelete"),
    url(r'^supprimer/prisencharge/(?P<pk>\d+)/$', views.PrisenchargeDeleteView.as_view(), name="PrisenchargeDeleteView"),
    url(r'^modifier/(?P<pk>\d+)/$', views.CircuitUpdate.as_view(), name="CircuitUpdate"),
    url(r'^nos_circuit/(?P<pk>\d+)/$', views.CircuitDetail.as_view(), name="CircuitDetail"),
    url(r'^info/modifier/(?P<pk>\d+)/$', views.HomeUpdate.as_view(), name='HomeUpdate'),
    url(r'^prisencharge/modifier/(?P<pk>\d+)/$', views.PrisenchargeUpdate.as_view(), name='PrisenchargeUpdate'),
    url(r'^infos/create/$', views.HomeInfo.as_view(), name='HomeInfor'),
    url(r'^prisencharge/Ajouter/$', views.Prisencharge.as_view(), name='Prisencharge'),
    url(r'^prisencharge/$', views.PrisenchargeList.as_view(), name='PrisenchargeList'),
    url(r'^ajouter/$',views.CirctuiCreate.as_view(),name="Circtuitest"),
    url(r'^$', views.CircuitList.as_view(), name="CircuitList"),
]