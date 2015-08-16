from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views., name='index'),
    url(r'^(?P<company_id>[0-9]+)$',views.companyProfile,name='companyProfile'),
    #url(r'^(?P<company_id>[0-9]+)/result$',views.result,name='result'),
    url(r'^(?P<company_id>[0-9]+)/apply$',views.apply,name='apply'),
	url(r'^$',views.listCompanies,name='listCompanies'),
    #url
]