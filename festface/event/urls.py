from django.urls import path
from . import views


urlpatterns = [
    path('',views.eventsindex,name="eventsindex"),
    path('events/<pk>',views.events,name="events"),
    path('addevent/',views.addevent,name="addevent"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('displayevent/<pk>',views.displayevent,name="displayevent"),
    path('registerevent/',views.registerevent,name="registerevent"),
    path('festmeta/',views.festmeta,name="festmeta"),
    path('displayfest/<pk>',views.displayfest,name="displayfest"),
    path('home/',views.home,name="home"),
    path('deletefest',views.deletefest,name="deletefest"),
    path('deleteevent',views.deleteevent,name="deleteevent"),
    path('editfest/<pk>',views.editfest,name="editfest"),
    path('viewregistrations/<pk>',views.viewregistrations,name="viewregistrations"),
    path('getregdetails/',views.getregdetails,name="getregdetails"),
]
