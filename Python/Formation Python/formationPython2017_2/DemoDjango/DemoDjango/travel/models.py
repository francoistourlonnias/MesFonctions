from django.db import models

# Create your models here.
def std_lookup(std_code):
    
    country_codes = { '44': 'United Kingdom' ,
                      '01': 'Canada and United States of America',
                      '33': 'France',
                      '46': 'Sweden',
                      '81': 'Japan' }
    
    if std_code in country_codes:
        data_for_view = {'std_country' : country_codes[std_code], 
                     'std_code' : std_code}
    else:
        data_for_view = {'std_country' : "Unknown country.  Sorry.", 
                     'std_code' : std_code}
        
    return (data_for_view)