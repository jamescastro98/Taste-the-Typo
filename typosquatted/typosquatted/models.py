from django.db import models

class webData(models.Model):
    name=models.CharField(max_length=150) #name of website - found in head of html doc as <title>NAME</title>
    origin=models.CharField(max_length=150) #original url (http://google.com , etc)
    typo=models.CharField(max_length=150) #typo'd urls