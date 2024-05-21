from django.contrib import admin
from django_celery_beat.models import PeriodicTask, IntervalSchedule


from .models import *
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Poste)
admin.site.register(Reaction)
admin.site.register(EventClub)
admin.site.register(EventSocial)
admin.site.register(Accommodation)
admin.site.register(Transport)
admin.site.register(Stage)
admin.site.register(Recommandation)

