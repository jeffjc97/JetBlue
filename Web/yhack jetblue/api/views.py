from django.shortcuts import render
from django.http import HttpResponse
from api.models import Getaway


# Create your views here.
def query(request, airports=None):
	airport_list = airports.split('&')
	gl = Getaway.objects.filter(flight_origin__in=airport_list)
	flights = []
	for g in gl:
		json = {'flight_origin':g.flight_origin, 'flight_dest':g.flight_dest, 'savings':g.savings}
		flights.append(json)
	response = HttpResponse(flights, content_type="application/json")
	return response
