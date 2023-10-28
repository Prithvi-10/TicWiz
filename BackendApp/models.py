from django.db import models
import datetime


# Create your models here.
class EventCategoryDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="Event_Category")

class SubeventDb(models.Model):
    Category_Name = models.CharField(max_length=50, null=True, blank=True)
    Subcategory_name = models.CharField(max_length=50,null=True,blank=True)
    Sub_description=models.CharField(max_length=500,null=True,blank=True)
    Sub_Image=models.ImageField(upload_to="Sub_Cattegory")

class MovieDB(models.Model):
    Category_name = models.CharField(max_length=50,null=True,blank=True)
    Subcategory_Name = models.CharField(max_length=50,null=True,blank=True)
    Movie_Name = models.CharField(max_length=50,null=True,blank=True)
    Movie_Description = models.CharField(max_length=500,null=True,blank=True)
    Movie_Cast=models.CharField(max_length=100,null=True,blank=True)
    Movie_Time=models.CharField(max_length=50,null=True,blank=True)
    Movie_Screen = models.CharField(max_length=50, null=True, blank=True)
    Show_Time = models.CharField(max_length=50, null=True, blank=True)
    Movie_Image = models.ImageField(upload_to="Movie")



class SportsDB(models.Model):
    Category_name = models.CharField(max_length=50, null=True, blank=True)
    Subcategory_Name = models.CharField(max_length=50, null=True, blank=True)
    Match_Info = models.CharField(max_length=100, null=True, blank=True)
    Match_Venue = models.CharField(max_length=50, null=True, blank=True)
    Match_Date = models.CharField(max_length=50, null=True, blank=True)
    Match_Time = models.CharField(max_length=50, null=True, blank=True)
    Match_Image = models.ImageField(upload_to="Sports")

class Bookingdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Seat = models.CharField(max_length=50,null=True,blank=True)
    Movie = models.CharField(max_length=100,null=True,blank=True)
    Screen = models.CharField(max_length=100,null=True,blank=True)
    Time = models.CharField(max_length=100,null=True,blank=True)
    Date = models.DateField(default=datetime.date.today)
    Price = models.IntegerField(null=True,blank=True)


# class BookingConfirm(models.Model):
#     Name = models.CharField(max_length=100,null=True,blank=True)
#     Seat = models.CharField(max_length=50,null=True,blank=True)
#     Movie = models.CharField(max_length=100,null=True,blank=True)
#     Screen = models.CharField(max_length=100,null=True,blank=True)
#     Time = models.CharField(max_length=100,null=True,blank=True)


class DetailsDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)

class admindb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=200,null=True,blank=True)
