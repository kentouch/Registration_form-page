from django.db import models

class Registration(models.Model):
    DELEGATE_CATEGORIES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        ('category3', 'Category 3'),
    ]

    SOCIAL_ACTIVITIES = [
        ('activity1', 'Activity 1'),
        ('activity2', 'Activity 2'),
        ('activity3', 'Activity 3'),
    ]

    delegate_category = models.CharField(max_length=50, choices=DELEGATE_CATEGORIES)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    nationality = models.CharField(max_length=30)
    national_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    organization = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    country_of_residence = models.CharField(max_length=30)
    social_activities = models.CharField(max_length=50, choices=SOCIAL_ACTIVITIES)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"