from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    user = models.ForeignKey(User, related_name='user_projects', null=True, blank=True)
    title = models.CharField('Title', max_length = 200)
    url = models.URLField(null=True,blank=True)
    description = models.TextField('Description',null=True,blank=True)
    logo = models.ImageField('Logo',upload_to='logos',null=True, blank=True)
        
    def __unicode__(self):
        return self.title
    
class Technologies(models.Model):
    user = models.ForeignKey(User, related_name='user_skills', null=True, blank=True)
    name = models.CharField('Name', max_length = 200)
    logo = models.ImageField('Logo',upload_to='logos',null=True, blank=True)
    order = models.IntegerField('Order',null=True, blank=True)
      
    def __unicode__(self):
        return self.name