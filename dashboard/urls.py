from django.urls import path

from . import views

urlpatterns = [

    path('dashboard', views.dashboard, name="dashboard"),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('',views.index,name='index'),
    path('events/<int:pk>',views.events,name='events'),
    path('team',views.team,name='team'),
    path('add_link',views.add_link,name='add_link'),
    path('link_table',views.link_table,name='link_table'),
    path('l/<str:key>',views.l,name='l'),

]