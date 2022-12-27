from django.db import models
from theaters.models import Theaters
from movies.models import Movies

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
    time = models.CharField(choices=TIME, max_length=50)
    date = models.DateField()
    total_tickets = models.IntegerField(default=50)
    is_tick_avail = models.BooleanField(default=True)

    def __str__(self):
        slug = self.movie.movie_title[:4] + self.theater.theater_name[:4] + str(self.time)
        return str(slug)





# class Seats(models.Model):
#     SEAT_CHOICE = (
#         ('A1', 'A1'),
#         ('A2', 'A2'),
#         ('A3', 'A3'),
#         ('A4', 'A4'),
#         ('A5', 'A5'),
#         ('A6', 'A6'),
#         ('A7', 'A7'),
#         ('A8', 'A8'),
#         ('A9', 'A9'),
#         ('A10', 'A10'),
#         ('B1', 'B1'),
#         ('B2', 'B2'),
#         ('B3', 'B4'),
#         ('B4', 'B4'),
#         ('B5', 'B5'),
#         ('B6', 'B6'),
#         ('B7', 'B7'),
#         ('B8', 'B8'),
#         ('B9', 'B9'),
#         ('B10', 'B10'),
#         ('C1', 'C1'),
#         ('C2', 'C2'),
#         ('C3', 'C4'),
#         ('C4', 'C4'),
#         ('C5', 'C5'),
#         ('C6', 'C6'),
#         ('C7', 'C7'),
#         ('C8', 'C8'),
#         ('C9', 'C9'),
#         ('C10', 'C10'),
#         ('D1', 'D1'),
#         ('D2', 'D2'),
#         ('D3', 'D4'),
#         ('D4', 'D4'),
#         ('D5', 'D5'),
#         ('D6', 'D6'),
#         ('D7', 'D7'),
#         ('D8', 'D8'),
#         ('D9', 'D9'),
#         ('D10', 'D10'),
#         ('E1', 'E1'),
#         ('E2', 'E2'),
#         ('E3', 'E4'),
#         ('E4', 'E4'),
#         ('E5', 'E5'),
#         ('E6', 'E6'),
#         ('E7', 'E7'),
#         ('E8', 'E8'),
#         ('E9', 'E9'),
#         ('E10', 'E10'),
#     )
    

#     STATUS = (
#         ('sold', 'sold'),
#         ('available', 'available'),
#         ('selected', 'selected'),
#     )
#     show = models.ForeignKey(MovieShow, on_delete=models.CASCADE, null=True)
#     seatname = models.CharField(choices=SEAT_CHOICE, unique=True, max_length=50)
#     status = models.CharField(choices=STATUS, max_length=10, default='available')

#     def __str__(self):
#         return self.seatname
    


