from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index,name="index"),
     path('/stages', Stage_listView.as_view(),name="liste_stages"),
     path('likes/<int:post_id>/', views.like, name='likes'),
     path('/AjouterStages', CreeStage.as_view(),name="cree_stage"),
     path('profile/', views.profile_view, name='profile'),
      path('update_profile/', views.update_profile, name='update_profile'),
      path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
       path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('get-notifications/', views.get_notifications, name='get_notifications'),
    path('/accommodations', accommodations_listView.as_view(),name="accommodations"),
    path('/AjouterAccommodations', CreeAccommodation.as_view(),name="cree_accommodation"),
     path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),

      path('<int:pk>/modifierA/', AccommodationUpdateView.as_view(), name='modifier_accommodation'), 
          path('/transports', transports_listView.as_view(),name="transports"),
       path('<int:pk>/updateT/', TransportUpdateView.as_view(), name='update_transport'),
    path('<int:pk>/deleteT/', TransportDeleteView.as_view(), name='delete_transport'),
    path('/AjouterTransport', CreeTransport.as_view(),name="cree_transport"),
     path('/recommandations', recommandations_listView.as_view(),name="recommandations"),
         path('/AjouterRecommandation', CreeRecommandation.as_view(),name="cree_recommandation"),
    path('<int:pk>/updateR/', RecommandationUpdateView.as_view(), name='update_recommandation'),
    path('<int:pk>/deleteR/', RecommandationDeleteView.as_view(), name='delete_recommandation'),
    path('<int:pk>/update/', StageUpdateView.as_view(), name='update_Stage'),
     path('notifications/', views.notifications_view, name='notifications'),
       path('notifications/mark-as-read/', mark_notifications_as_read, name='mark_notifications_as_read'),
    path('notifications/mark-as-read/<int:notification_id>/', views.mark_single_notification_as_read, name='mark_single_notification_as_read'),
]

  
