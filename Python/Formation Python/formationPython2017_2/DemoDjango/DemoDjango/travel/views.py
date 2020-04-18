# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello World")

import country_code_lookup

def get_std_country( request, std_code):
    # call model
    results = country_code_lookup.find_code(std_code)
    
    data_for_view = {'std_country' : results[std_code], 
                     'std_code' : std_code}
  
    return  render_to_response('std_country_code.html', data_for_view)

