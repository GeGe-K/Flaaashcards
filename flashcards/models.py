from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_subject(self):
        self.save()

    def delete_subject(self):
        self.delete()

class Card(models.Model):
    title = models.CharField(max_length=30)
    notes = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def save_card(self):
        self.save()

    def delete_card(self):
        self.delete()
    
    @classmethod
    def get_all_cards(cls):
        cards = cls.objects.all()
        return cards

    @classmethod
    def get_card(cls, id):
        card = cls.objects.get(id=id)
        return card
    
    @classmethod
    def filter_by_subject(cls, id):
        cards = cls.objects.filter_by_subject(subject__id=id)
        return cards

    @classmethod
    def search_card(cls, search_term):
        cards = cls.objects.filter(subject__name__icontains=search_term)
        return cards

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='photos', null=True, blank=True)
    bio = models.TextField(blank=True)
    contacts = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

    
