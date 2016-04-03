from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^login/$', views.login, name='login'),
    url(r'^tables/$', views.tables, name='tables'),
    url(r'^morris/$', views.morris, name='morris'),
    url(r'^flot/$', views.flot, name='flot'),
    url(r'^forms/$', views.forms, name='forms'),
    url(r'^results/$', views.results, name='results'),

]
