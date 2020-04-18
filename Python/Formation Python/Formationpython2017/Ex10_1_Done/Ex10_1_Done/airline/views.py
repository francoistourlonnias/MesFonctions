# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello World")

import airlineLookup

def getCityCode(request, cityCode):
    # call model
    cityCode = cityCode.upper()
    results = airlineLookup.findCity(cityCode)
    
    displayDict = {'city' : results[cityCode], 
                     'cityCode' : cityCode}
  
    return  render_to_response('airport_code.html', displayDict)


def getReservation(request, reservationId):
    # call model
    reservationId = int(reservationId)
    results = airlineLookup.findReservation(reservationId)
    
    displayDict = {'reservation' : results[reservationId], 
                     'reservationId' : reservationId}
  
    return  render_to_response('reservation.html', displayDict)