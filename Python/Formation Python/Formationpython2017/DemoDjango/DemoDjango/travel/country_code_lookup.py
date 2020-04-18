'''
country_code_lookup.py
A module that does a dictionary lookup
'''


country_codes = { '44': 'United Kingdom' ,
                '01': 'Canada and United States of America',
                '33': 'France',
                '46': 'Sweden',
                '81': 'Japan' }

def find_code(code):
    if country_codes.get(code):
        d = {code:country_codes[code]}
    else:
        errorMsg = 'Unknown country code'
        d = {code:errorMsg}
    return(d)