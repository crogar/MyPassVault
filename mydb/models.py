from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):  # inheriting from models --- Topic is Service field in Database
    topic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name


class Account(models.Model):  # this will handle the Website Name and URL
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)  # Service in database
    Email = models.CharField(max_length=100)  # Email in database
    website_name = models.CharField(max_length=100)  # website_name in database
    url = models.URLField(unique=False)  # website in database
    password = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    comment = models.CharField(max_length=1500)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=250)  # Address in database
    Phone_Number = models.CharField(max_length=25)  # Phone Number in database

    def __str__(self):
        return self.url


class AccessRecord(models.Model):
    name = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


##########################################################################
# Creating User Model                                                    #
##########################################################################

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


##########################################################################
# Creating User Model                                                    #
##########################################################################
