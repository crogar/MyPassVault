from django.db import models


# Create your models here.

class Topic(models.Model):  # inheriting from models --- Topic is Service field in Database
    topic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name


class Account(models.Model):  # this will handle the Website Name and URL
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)  # Service in database
    Email = models.CharField(max_length=100)  # Email in database
    Address = models.CharField(max_length=250)  # Address in database
    PhoneNumber = models.CharField(max_length=25)  # Phone Number in database
    website_name = models.CharField(max_length=100)  # website_name in database
    url = models.URLField(unique=True)  # website in database
    password = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.url
