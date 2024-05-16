from django.urls import reverse_lazy
from django.views.generic import *
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
def index(request):
    return render( request,'student_help/index.html' )
def stages(request):
    stages =Stage.objects.all()
    context={'stages':stages}
    return render( request,'student_help/stages.html',context )
class Stage_listView(ListView):
    model = Stage
    template_name = 'student_help/liste_stages.html'
    context_object_name = 'stages'
class CreeStage(CreateView):
    model = Stage
    template_name = 'student_help/cree_stage.html'
    form_class = StageForm 
    success_url = reverse_lazy('liste_stages')   

