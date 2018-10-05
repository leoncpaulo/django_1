from django.db import models
from django.utils import timezone

# class Post has-a list of object properties & takes Model parameter from models 
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField (max_length=200) 
    text = models.TextField ()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField (blank = True, null = True)

# publish function/method takes self parameter and defines two methods
    def publish (self):
        self.published_date = timezone.now()
        self.save()
 # gets a Post title   
    def _str_ (self):
        return self.title



