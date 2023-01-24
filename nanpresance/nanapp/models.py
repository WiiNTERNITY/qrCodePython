from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from _datetime import datetime
from django.utils.text import slugify
from datetime import date,datetime,time, timedelta
from django.utils.timezone import now
import pytz


# Create your models here.
GROUPE_CHOICES = ( 
    ("A", "A"), 
    ("B", "B"), 

) 
#-------- ETUDIANT --------#

class Jour(models.Model):
    nom = models.CharField(max_length = 225)
    
    def __str__(self):
        return str( self.nom)
class Groupe(models.Model):
    nom = models.CharField(
            max_length = 20, 
            choices = GROUPE_CHOICES, 
            default = 'A',
            unique = True
    )
    jour_passage = models.ManyToManyField(Jour, related_name="jour")
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    




    def __str__(self):
        return str( self.nom)
#-------- ETUDIANT --------#
class Profile(models.Model):
    """Model definition for Profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    contacts = models.CharField(max_length=30, null=True,  blank=True)
    genre = models.CharField(max_length=20, null=True, blank=True)
    groupe = models.ForeignKey(Groupe ,on_delete=models.CASCADE, related_name="user_groupe",null=True , blank=True )
    birth_date = models.DateField(null=True, blank=True)
    images = models.ImageField(upload_to='images/avatar/', default="photo.png")
    specialite = models.CharField(max_length=255,null=True, blank=True)
    is_admin = models.BooleanField(default=False,null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user_profile.save()
    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.username

#----------- JOURS -----------------#

 
class Qrcode(models.Model):
    jours = models.CharField(editable=False,null=True,max_length=255)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True,related_name= 'addby')
    debut_heure_arrivee = models.TimeField(null=True, default='08:00')
    fin_heure_arrivee = models.TimeField(null=True, default='10:00')
    titre_slug = models.SlugField(max_length=255,null=True,unique=True)
    status =  models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str( self.jours)

    @property
    def is_valid(self):
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
            
        if self.debut_heure_arrivee.strftime("%H:%M:%S") < current_time  and self.fin_heure_arrivee.strftime("%H:%M:%S") > current_time:
            
            return True
        else :
            return False
    
    def save(self, *args, **kwargs):
            
        super(Qrcode, self).save(*args, **kwargs)


        self.jours = date.today()    
        super(Qrcode, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Exercice."""

        verbose_name = 'QrCode'
        verbose_name_plural = 'QrCodes'
        ordering = ('created_at',)

class Presence(models.Model):
    jour = models.CharField(editable=False,null=True,max_length=255)
    etudiant = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, related_name='userpresence')
    qrcode = models.ForeignKey(Qrcode, on_delete=models.CASCADE, related_name='joursap')
    heure_arrivee = models.TimeField(null=True)
    heure_depart = models.TimeField(null=True, default='17:00')
    status = models.BooleanField(default=False)
    status =  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('etudiant', 'qrcode',)

    def save(self, *args, **kwargs):
 
        super(Presence, self).save(*args, **kwargs)
        self.jour = date.today()
        super(Presence, self).save(*args, **kwargs)