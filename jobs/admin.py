from django.contrib import admin
from .models import Job  #Job is the name of the class created in the models.py file 

admin.site.register(Job)

#in the calss Job we have created two models like images and summry and both of these will appear in the admin page

