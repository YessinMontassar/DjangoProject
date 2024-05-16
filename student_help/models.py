import datetime
from django.db import models
#class User :

class User(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    telephone =models.CharField(max_length=8)
    email = models.EmailField()
    def __str__(self)  :
        return self.name

#class Poste :

class Poste(models.Model):
    image = models.ImageField()
    type = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    
    def __str__(self):
        return str(self.type)
     

#class Reaction :

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

class Stage (Poste):
    typeStg = models.IntegerField()
    company = models.CharField(max_length=100)
    period = models.IntegerField()
    topic = models.CharField(max_length=100)
    contactInfo= models.CharField(max_length=100)
    specialty=models.CharField(max_length=100)
   

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