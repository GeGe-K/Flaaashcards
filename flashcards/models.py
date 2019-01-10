from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_subject(self):
        self.save()

    def delete_subject(self):
        self.delete()

class Profile(models.Model):
    
    '''
    A class to allow users to update and view their profile
    '''
    bio = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    Flashcard = models.ForeignKey('Flashcard',on_delete=models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

class Flashcard(models.Model):

    '''
    A class that allows users to post,view and rate projects
    '''
    
    title = models.CharField(max_length=20)
    notes = HTMLField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

    def save_flashcard(self):
        self.save()

    def delte_flashcard(self):
        self.delete()

    @classmethod
    def update_flashcard(self):
        update_flashcard = cls.objects.filter(id=id).update(notes=notes)
        return flashcard
    
    @classmethod
    def filter_by_subject(cls, id):
        flashcard = cls.object.filter_by_subject(subject__id=id)
        return flashcard


