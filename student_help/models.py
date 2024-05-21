import datetime
from django.contrib.auth.models import User
from django.db import models
#class Poste :

class Poste(models.Model):
    image = models.ImageField(blank=True)
    type = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.type)
     

#class Reaction :
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    poste = models.ForeignKey(Poste, related_name='likes_received', on_delete=models.CASCADE, null=True)

class Reaction(models.Model):
    comment = models.TextField()
    like = models.BooleanField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    react = models.ForeignKey(Poste,on_delete=models.CASCADE)


#class Event :

class Event(Poste):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    contactInfo= models.CharField(max_length=100)

#class EventClub :

class EventClub(Event):
    club = models.CharField(max_length=100)
  
#class EventSocial :

class EventSocial(Event):
    prix = models.DecimalField(max_digits=10,decimal_places=3)
#class Stage :
class Stage(Poste):
    OUVRIER = 1
    TECHNICIEN = 2
    PFE = 3

    TYPE_CHOICES = [
        (OUVRIER, 'Ouvrier'),
        (TECHNICIEN, 'Technicien'),
        (PFE, 'PFE'),
    ]

    typeStg = models.IntegerField(choices=TYPE_CHOICES)
    company = models.CharField(max_length=100)
    period = models.IntegerField()
    topic = models.CharField(max_length=100)
    contactInfo = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
   

#class Accommodation :

class Accommodation(Poste):
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    contactInfo = models.CharField(max_length=100)

#class Transport :

class Transport(Poste):
    begin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    hourBegin = models.TimeField()
    nbrSeat = models.IntegerField()

#class Recommandation :

class Recommandation(Poste):
    text = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='../media/profile_pictures/yessin.jpg',blank=True, null=True)

    def __str__(self):
        return self.user.username    
    @property
    def posts(self):
        return self.user.blog_posts.all()
class Comment(models.Model):
    post = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)   
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message     