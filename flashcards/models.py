from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from django.contrib.auth.models import User

class Profile(models.Model):
    '''A class to allow users to update and view their profile
        '''
    description = HTMLField()
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
    '''A class that allows users to post,view and rate projects
        '''
    
    title = models.CharField(max_length=20)
    description = HTMLField()
    subject = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_card(self):
        self.save()
    def delte_card(self):
        self.delete()

    @classmethod
    def update_card(self):
        update_card = cls.objects.filter(id=id).update(description=description)
        return update
    def __str__(self):
        return self.user.username