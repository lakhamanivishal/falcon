from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('portfolio/',views.portfolio,name='portfolio'),
   path('signup/',views.signup,name='signup'),
   path('login/',views.login,name='login'),
   path('falcon/',views.falcon,name='falcon'),
   path('rhinofact/',views.rhinofact,name='rhinofact'),
   path('butterfly/',views.butterfly,name='butterfly'),
   path('tiger/',views.tiger,name='tiger'),
   path('vultures/',views.vultures,name='vultures'),
   path('lion/',views.lion,name='lion'),
]
