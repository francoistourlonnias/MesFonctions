# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello World")

import airlineLookup

def getCityCode( request, cityCode):

    cityCode = cityCode.upper() # convert to upper case
    # call model method below, assign returned value into a dictionary
    
    
    # create a dictionary of values returned from the model method
    # keys are used in the HTML template file
    
    displayDict = {}
  
    return  render_to_response('airport_code.html', displayDict)

