from django.db import models

# Create your models here.

class Theaters(models.Model):

    district_choices = (
        ('TVM', 'Trivandrum'),
        ('EKM', 'Eranakulam'),
        ('kZH', 'Kozhikode'),
    )

    theater_name = models.CharField(max_length=50)
    about_theater = models.TextField(max_length=350, blank=True)
    landmark_1 = models.CharField(max_length=50)
    landmark_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25)
    district = models.CharField(max_length=50, choices=district_choices)
    state = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=25)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.theater_name
