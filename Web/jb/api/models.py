from django.db import models
# from common import enum

# Create your models here.
# class AdvanceType(enum.Enum):
#     short = enum.Item(1, "Within 1 week")
#     medium = enum.Item(2, "1 to 2 weeks")
#     long = enum.Item(3, "2 to 4 weeks")

class Getaway(models.Model):
	flight_origin = models.CharField(max_length=10)
	flight_dest = models.CharField(max_length=10)
	hotel = models.CharField(max_length=300)
	nights = models.IntegerField()
	check_in = models.DateField()
	check_out = models.DateField()
	expedia_price = models.DecimalField(decimal_places=2, max_digits = 10)
	jetblue_price = models.DecimalField(decimal_places=1, max_digits = 10)
	savings = models.DecimalField(decimal_places=1, max_digits = 4)
	advance_weeks = models.IntegerField()
	# advance_weeks = models.IntegerField(choices=AdvanceType)