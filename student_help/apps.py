from django.apps import AppConfig


class StudentHelpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_help'

    def ready(self):
        import student_help.signals
