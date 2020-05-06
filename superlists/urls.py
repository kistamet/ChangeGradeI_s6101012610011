from django.conf.urls import url
from lists import views
from django.urls import path, include
from django.contrib import admin


#from superlists

urlpatterns = [
    path('', views.register, name='register'),
    path('calGrade', views.calGrade,name='calGrade'),
    path('admin/', admin.site.urls),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'home', views.home_page, name='home'),
    url(r'flow', views.flow, name='flow'),
    url(r'help', views.help, name='help'),
    url(r'subject', views.listOfSubject, name='listOfSubjects'),
    url(r'graph', views.Graph, name='Graph'),
    url(r'picFlow', views.picFlow, name='picFlow'),
    url('result', views.result, name='result'),
    url(r'about', views.about, name='about'),
]
