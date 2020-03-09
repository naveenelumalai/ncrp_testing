from django.db import models

# Create your models here.

class CyberStories(models.Model):
    StoryID = models.CharField(max_length=264)
    Title = models.CharField(max_length=264)
    Link = models.CharField(max_length=264)
    Published = models.DateField()
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.StoryID

class NCRPComplaints(models.Model):
    NCRPNumber = models.CharField(max_length=15)
    ComplaintDistrict = models.CharField(max_length=30)
    ComplaintPoliceStation = models.CharField(max_length=264,null=True)
    ComplaintCategory = models.CharField(max_length=264,null=True)
    ComplaintSubCategory = models.CharField(max_length=264,null=True)
    AccusedPhoneNumber = models.CharField(max_length=264)
    AccusedEmailID = models.CharField(max_length=50,null=True)
    ActionTaken = models.CharField(max_length=264,null=True)
    FIRorCSRNumber = models.CharField(max_length=264,null=True)
    ComplaintAction = models.CharField(max_length=264,null=True)



    def __str__(self):
        return self.NCRPNumber
