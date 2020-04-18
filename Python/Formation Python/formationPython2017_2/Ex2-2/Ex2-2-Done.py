"""
Exercise 2.2 Strings and if.
"""

# Part A
plane1 = 'Boeing767 6670'
plane2 = 'CRJ        950'

p1type = plane1[:9]
p2type = plane2[:9]

p1miles = plane1[9:]
p2miles = plane2[9:]

print "plane1's type is", p1type, 'it flies', p1miles, 'miles'
print "plane2's type is", p2type, 'it flies', p2miles, 'miles'

totaltype = p1type + p2type 
print 'The concatenation of all plane types is', totaltype

totalmiles = int(p1miles) + int(p2miles) 
print 'The total miles from all planes is', totalmiles

totalcsv = p1type + ',' + p1miles + ',' + p2type + ',' + p2miles 
print 'The CSV values of planes and miles is', totalcsv


# Part B
plane1 = 'Boeing767,6670'
plane2 = 'CRJ,950'

comma = plane1.find(',')
p1type = plane1[:comma]
p1miles = plane1[comma + 1:]

comma = plane2.find(',')
p2type = plane2[:comma]
p2miles = plane2[comma + 1:]

print "plane1's type is", p1type, 'it flies', p1miles
print "plane2's type is", p2type, 'it flies', p2miles


# Part C

print 'The all uppercase plane type is'
if p1type.isupper():
    print p1type

if p2type.isupper():
    print p2type
    
print 'The plane type that ends is a digit is'
if p1type[-1].isdigit():
    print p1type

if p2type[-1].isdigit():
    print p2type

print 'The plane that travels farther is'
if int(p1miles) > int(p2miles):
    print p1type, p1miles
else:
    print p2type,p2miles

# Part D

print """Python is Guido's invention"""
print '''They say "Guido is the BDFL"'''
print '''They say "Guido is the 'BDFL'"'''

airport1 = "HNL,Honolulu"
airport2 = "LHR,London/Heathrow"
airport3 = "ARN,Stockholm/Arlanda"
airport4 = "HKG,Hong Kong"
airport5 = "GCM,Grand Cayman BWI"

dubquote = '"'
sep = ','
comma = airport1.find(',')
airports = dubquote + airport1[:comma] + dubquote + sep

comma = airport2.find(',')
airports =  airports + dubquote + airport2[:comma]+ dubquote + sep
    
comma = airport3.find(',')
airports = airports + dubquote  + airport3[:comma]+ dubquote + sep

comma = airport4.find(',')
airports = airports + dubquote  + airport4[:comma]+ dubquote + sep

comma = airport5.find(',')
airports = airports + dubquote  + airport5[:comma]+ dubquote

print 'Airport codes', airports

comma = airport1.find(',')
airports = dubquote + airport1[comma+1:] + dubquote + sep

comma = airport2.find(',')
airports =  airports + dubquote + airport2[comma+1:]+ dubquote + sep
    
comma = airport3.find(',')
airports = airports + dubquote  + airport3[comma+1:]+ dubquote + sep

comma = airport4.find(',')
airports = airports + dubquote  + airport4[comma+1:]+ dubquote + sep

comma = airport5.find(',')
airports = airports + dubquote  + airport5[comma+1:]+ dubquote

print 'Airport names', airports
