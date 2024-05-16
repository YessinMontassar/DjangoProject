from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index,name="index"),
     path('/stages', Stage_listView.as_view(),name="liste_stages"),
     path('/AjouterStages', CreeStage.as_view(),name="cree_stage"),
   ]
