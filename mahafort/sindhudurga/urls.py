from django.urls import include, re_path,path
from sindhudurga import views

urlpatterns = [
    re_path(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    re_path(r'^about/$', views.AboutPageView.as_view(), name='about'),
    re_path(r'^data/$', views.DataPageView.as_view(), name='data'),
    re_path(r'^contactus/$', views.ContactUsPageView.as_view(), name='contactus'),
    path('staticstring', views.PlainText,name='staticstring'),
    path('form', views.FormView,name='form'),
]