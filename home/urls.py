from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("prediction",views.prediction,name='prediction'),
    path("revenue",views.revenue,name='revenue'),
    path("revenueprediction",views.revenueprediction,name='revenueprediction')

]
