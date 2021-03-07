def print_german(name):
    print 'Guten Morgen! ', name

def print_italian(name):
    print 'Buon Giorno ! ', name   

def print_greeting(lang, printer):
    print 'Good Morning in ', lang, 'is ', 
    printer()

print_greeting('German', lambda: print_german('Hans'))
print_greeting('Italian', lambda: print_italian('Gina'))    