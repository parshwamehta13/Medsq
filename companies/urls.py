from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^companyList/(?P<company_id>[0-9]+)$',views.companyProfile,name='companyProfile'),
    url(r'^(?P<company_id>[0-9]+)/result$',views.result,name='result'),
    url(r'^(?P<company_id>[0-9]+)/applied$',views.applied,name='applied'),
    url(r'^companyList$',views.listCompanies,name='listCompanies'),
]