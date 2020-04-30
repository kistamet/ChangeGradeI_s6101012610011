from django.conf.urls import url
from lists import views
from django.urls import path, include
from django.contrib import admin


#from superlists

urlpatterns = [
    path('', views.register, name='register'),
    path('calGrade', views.calGrade,name='calGrade'),
#    path('termselect', views.termselect,name='termselect'),
    path('admin/', admin.site.urls),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'home', views.home_page, name='home'),
    url(r'flow', views.flow, name='flow'),
    url(r'help', views.help, name='help'),
    url(r'subject', views.listOfSubject, name='listOfSubjects'),
    url(r'graph', views.Graph, name='Graph'),
#    url(r'result', views.Result, name='Result'),
    url(r'picFlow', views.picFlow, name='picFlow'),
    url(r'firstTerm', views.firstTerm, name='firstTerm'),
    url(r'secondTerm', views.secondTerm, name='secondTerm'),
    url(r'thirdTerm', views.thirdTerm, name='thirdTerm'),
    url(r'fourthTerm', views.fourthTerm, name='fourthTerm'),
    url(r'fifthTerm', views.fifthTerm, name='fifthTerm'),
    url(r'sixthTerm', views.sixthTerm, name='sixthTerm'),
    url(r'seventhTerm', views.seventhTerm, name='seventhTerm'),
    url(r'eightTerm', views.eightTerm, name='eightTerm'),
    url(r'about', views.about, name='about'),
    #url(r'home', views.home_page, name='calGrade'),
    #admin page
    #path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    #register path
    #path("register/", v.register, name="register"),


]
