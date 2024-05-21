from django.urls import reverse_lazy,reverse
from django.views.generic import *
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.utils.decorators import method_decorator

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
   
def index(request):
    unread_notification_count = get_unread_notification_count(request.user)
    return render( request,'student_help/index.html',{'unread_notification_count': unread_notification_count}, )
def stages(request):
    stages =Stage.objects.all()
    context={'stages':stages}
    unread_notification_count = get_unread_notification_count(request.user)
    return render( request,'student_help/stages.html',context ,{'unread_notification_count': unread_notification_count})
class Stage_listView(ListView):
    model = Stage
    template_name = 'student_help/liste_stages.html'
    context_object_name = 'stages'
@method_decorator(login_required, name='dispatch')    
class CreeStage(CreateView):
    model = Stage
    template_name = 'student_help/cree_stage.html'
    form_class = StageForm 
    success_url = reverse_lazy('liste_stages') 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreeStage, self).form_valid(form)  
def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('index')
        else :
            form = UserCreationForm()
            return render(request,'registration/register.html',{'form' : form})
@login_required
def like(request, post_id):
    post = Poste.objects.get(id=post_id)
    current_likes = post.likes
    user = request.user
    liked = Like.objects.filter(user=user, poste_id=post.id).count()

    if not liked:
        Like.objects.create(user=user, poste_id=post.id)
        current_likes += 1

    else:
        Like.objects.filter(user=user, poste_id=post.id).delete()
        current_likes -= 1

    post.likes = current_likes
    post.save()
    return HttpResponseRedirect(reverse('liste_stages'))
@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')  # Remplacez par le nom de votre vue de profil
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'student_help/update_profile.html', {'profile_form': profile_form})
@login_required
def profile_view(request):
    profile = request.user.profile
    posts = profile.posts
    return render(request, 'student_help/profile.html', {'profile': profile, 'posts': posts})
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Poste, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            post_user = comment.post.user
            message = f" {request.user.username} a commenté votre poste."
            create_notification(user=post_user, message=message)
            return redirect('post_detail', post_id=post.id)  # Redirige vers la vue de détail du poste
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form, 'post': post})

def modal_content(request):
    return render(request, 'comment.html')
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Poste, id=post_id)
    return render(request, 'student_help/post_detail.html', {'post': post})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.user == comment.user:
        comment.delete()
        return redirect('post_detail', post_id=post_id)
    else:
        return redirect('post_detail', post_id=post_id)
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})    
def create_notification(user, message):
    Notification.objects.create(user=user, message=message)


def get_notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False)
        notifications_data = [{'message': notification.message, 'created_at': notification.created_at} for notification in notifications]
        return JsonResponse({'notifications': notifications_data})
    else:
        return JsonResponse({'notifications': []})
def mark_notifications_as_read(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False)
        notifications.update(is_read=True)
    return JsonResponse({'success': True})  

def get_unread_notification_count(user):
    if user.is_authenticated:
        return Notification.objects.filter(user=user, is_read=False).count()
    else:
        return 0  

def list_accommodations(request):
    accommodations = Accommodation.objects.all()
    return render(request, 'student_help/accommodations.html', {'accommodations': accommodations})
class accommodations_listView(ListView):
    model = Accommodation
    template_name = 'student_help/accommodations.html'
    context_object_name = 'accommodations'
class CreeAccommodation(CreateView):
    model = Accommodation
    template_name = 'student_help/cree_accommodation.html'
    form_class = AccommodationForm 
    success_url = reverse_lazy('accommodations') 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreeAccommodation, self).form_valid(form)  


class StageUpdateView(UpdateView):
    model = Stage
    form_class = StageForm
    template_name = 'student_help/stage_form.html'
    success_url = reverse_lazy('liste_stages')    
               
    
def delete_post(request, post_id):
    post = get_object_or_404(Poste, id=post_id)
    if request.user == post.user:
        post.delete()
        return redirect('index')
    else:
        return redirect('index')   
class AccommodationUpdateView(UpdateView):
    model = Accommodation
    form_class = AccommodationForm
    template_name = 'student_help/modifier_accommodation.html'
    success_url = reverse_lazy('accommodations')

class RecommandationUpdateView(UpdateView):
    model = Recommandation
    form_class = RecommandationForm
    template_name = 'student_help/modifier_recommandation.html'
class EventClubUpdateView(UpdateView):
    model = EventClub
    form_class = EventClubForm
    template_name = 'student_help/modifier_eventclub.html'
class EventSocialUpdateView(UpdateView):
    model = EventSocial
    form_class = EventSocialForm
    template_name = 'student_help/modifier_eventsocial.html'    
def list_transports(request):
    transports = Transport.objects.all()
    return render(request, 'student_help/transports.html', {'transports': transports})
class transports_listView(ListView):
    model = Transport
    template_name = 'student_help/transports.html'
    context_object_name = 'transports'
class CreeTransport(CreateView):
    model = Transport
    template_name = 'student_help/cree_transport.html'
    form_class = TransportForm 
    success_url = reverse_lazy('transports') 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreeTransport, self).form_valid(form)     
class TransportDeleteView(DeleteView):
    model = Transport
    template_name = 'student_help/DeleteTransport.html'
    success_url = reverse_lazy('transports')  
class TransportUpdateView(UpdateView):
    model = Transport
    form_class = TransportForm
    template_name = 'student_help/transport_update.html'
    success_url = reverse_lazy('transports')



class recommandations_listView(ListView):
    model = Recommandation
    template_name = 'student_help/recommandations.html'
    context_object_name = 'recommandations'
class CreeRecommandation(CreateView):
    model = Recommandation
    template_name = 'student_help/cree_recommandations.html'
    form_class = RecommandationForm 
    success_url = reverse_lazy('recommandations') 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreeRecommandation, self).form_valid(form)        
class RecommandationUpdateView(UpdateView):
    model = Recommandation
    form_class = RecommandationForm
    template_name = 'student_help/recommandation_update.html'
    success_url = reverse_lazy('recommandations')

class RecommandationDeleteView(DeleteView):
    model = Recommandation
    template_name = 'student_help/recommandation_confirm_delete.html'
    success_url = reverse_lazy('recommandations')
@login_required
def notifications_view(request):
    unread_notifications = Notification.objects.filter(user=request.user, is_read=False)
    read_notifications = Notification.objects.filter(user=request.user, is_read=True)
    return render(request, 'student_help/notifications.html', {
        'unread_notifications': unread_notifications,
        'read_notifications': read_notifications
    })   
@login_required
def mark_single_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications')
 





