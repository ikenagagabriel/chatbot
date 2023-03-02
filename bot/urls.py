from django.urls import path
from django.conf.urls import url
from django.contrib import admin


from . import views

app_name = 'bot'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    url(r'^$', views.ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/chatterbot/', views.ChatterBotApiView.as_view(), name='chatterbot'),
]