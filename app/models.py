from django.db import models
from datetime import date

# Create your models here.
class blood(models.Model):
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20)
    Age=models.IntegerField(null=True)
    Bloodgroupchoices=[
        ('A+ve','A+ve'),
        ('B+ve','B+ve'),
        ('AB+ve','AB+ve'),
        ('O+ve','O+ve')
    ]
    Bloodgroup=models.CharField(choices=Bloodgroupchoices,max_length=25,null=True)
    Date=models.DateField(null=True)
    
    def _str_(self):
        return self.Name  

    '''def getdate(self):
        end = date.today()
        start = self.Date
        res = (end.year - start.year) * 12 + (end.month - start.month)+(end.day-start.day)/30
        
        if (res>=3):
            return "Available"
        else:
            return "Not available"

    datediff=property(getdate)'''
    
    '''
    
class signupform(models.Model):
    Username=models.CharField(max_length=20) 
    Email=models.EmailField(max_length=15)
    password=models.CharField(max_length=15)

def _str_(self):
        return self.Name     
    
  '''     
    '''def availability(self):
        hello=(date.today()-self.Date).days
        if(hello>=90):
            return "Available"
        else:
            return "Not Available"'''