from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100) #Title of note
    content = models.TextField() #Text field for note
    created_at = models.DateTimeField(auto_now_add=True) #Automatically add the date create automatically
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") #Linking with user. If we delete this user, we delete all the notes (models.CASCADE). In User class, we can use user.notes to access all the notes by the user
    

    def __str__(self):
        return self.title