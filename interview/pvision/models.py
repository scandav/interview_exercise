from django.db import models
import datetime


class Patient(models.Model):
    def __str__(self):
        return self.name

    UNKNOWN = 0
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (UNKNOWN, 'Unknown'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    name = models.CharField(max_length=256)
    birthdate = models.DateField(default=datetime.datetime.fromtimestamp(0))
    gender = models.IntegerField(choices=GENDER_CHOICES, default=UNKNOWN)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=256)


class Location(models.Model):
    """
    Create a Location model here. Include name of the hospital/clinician and address.
    Relate each measurement to the specific location:
    - One patient can go different locations
    - Each location has many patients
    """
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)


class Measurement(models.Model):
    LEFT = 1
    RIGHT = 2
    UNKNOWN = 0

    EYE_CHOICES = (
        (LEFT, 'left'),
        (RIGHT, 'right'),
        (UNKNOWN, 'Unknown')
    )

    def result_default():
        return {'values': [], 'mean_defect': 0.0, 'mean_sensitivity': 0.0}

    eye = models.IntegerField(choices=EYE_CHOICES, default=UNKNOWN)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.fromtimestamp(0))
    result = models.JSONField(default=result_default)
    program = models.CharField(default='NaN', max_length=2560)
    comment = models.CharField(default='', blank=True, max_length=2560)
    measurement_done = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
