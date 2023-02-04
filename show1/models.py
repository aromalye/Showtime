from django.db import models
from theaters.models import Theaters
from movies.models import Movies
from multiselectfield import MultiSelectField



# Create your models here.

class MovieShow(models.Model):

    TIME = (
        ('6:30 AM', '6:30 AM'),
        ('10:30 AM', '10:30 AM'),
        ('2:30 PM', '2:30 PM'),
        ('6:30 PM', '6:30 PM'),
        ('10:30 PM', '10:30 PM'),
    )

    theater = models.ForeignKey(Theaters, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    time = models.CharField(choices=TIME, max_length=100, null=True)
    date = models.DateField()
    total_tickets = models.IntegerField(default=50)
    is_tick_avail = models.BooleanField(default=True)

    def __str__(self):
        slug = self.movie.movie_title[:4] + self.theater.theater_name[:4] + str(self.time)
        return str(slug)





class Seats(models.Model):
    SEAT_ALPH = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    

    STATUS = (
        ('sold', 'sold'),
        ('available', 'available'),
        ('selected', 'selected'),
    )

    SEAT_NO= (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )

    show = models.ForeignKey(MovieShow, on_delete=models.CASCADE, null=True)
    seatnum = models.IntegerField(choices=SEAT_NO, null=True)
    seatalp = models.CharField(choices=SEAT_ALPH, max_length=1, null=True)
    status = models.CharField(choices=STATUS, max_length=10, default='available')

    def seatname(self):
        return self.seatalp + str(self.seatnum)
    


