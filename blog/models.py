from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length= 255)
    pub_date = models.DateTimeField()
    description= models.TextField()
    image= models.ImageField(upload_to= 'images/')

    def __str__(self):
        return self.title  #to modify the names of the titles in admin page. 


    def summary(self):
        return self.description[:70]

    def modified_date(self):
        return self.pub_date.strftime('%b %e %Y')  
        
#strftime is used to modify the time and date. %b is abbreviated month name, %e is the day of the month and %Y is year including Century 
