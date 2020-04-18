"""
Exercise 2.1 Simple Arithmetic.
"""

# Part A
ans = 5 / 9
print 'Integer division result is', ans

ans = 5.0 / 9.0
print 'Floating point division result is', ans


# Part B
ctof = 9.0 / 5.0
ftoc = 5.0 / 9.0
freezing = 32


Paris = '25'
Honolulu = '81'

Paris = int(Paris)
Honolulu = int(Honolulu)

ParisF = Paris * ctof + freezing
HonoluluC = ( Honolulu - freezing ) * ftoc

print 'The Celsius temperature in Paris is', Paris
print 'The Fahrenheit temperature in Paris is', ParisF
print 'The Fahreneit temperature in Honolulu is', Honolulu
print 'The Celsius temperature in Honolulu is', HonoluluC

# Part C
price = 199.95

discountA = .05
discountB = .10
discountC = .15

priceA = price - ( price * discountA )
priceB = price - ( price * discountB )
priceC = price - ( price * discountC )

print 'The original price is', price
print 'The price with discountA', discountA, 'is %5.2f' % priceA
print 'The price with discountB', discountB, 'is %5.2f' % priceB
print 'The price with discountC', discountC, 'is %5.2f' % priceC


# Part D

d1 = 18.7
d2 = 27.9
t1 = 62.1
t2 = 91.2
mtok = 1.6

print 'the speed for ride 1 in miles per hour is %5.2f' % ( d1 / t1 * 60 )
print 'the speed for ride 1 in kilometers per hour is %5.2f' % ( d1 / t1 * 60 * mtok)
print 'the speed for ride 2 in miles per hour is %5.2f' % ( d2 / t2 * 60 )
print 'the speed for ride 2 in kilometers per hour is %5.2f' % ( d2 / t2 * 60 * mtok )

avg = ( d1 + d2 ) / ( t1 + t2 ) * 60
print 'the average speed for both rides in miles per hour is %5.2f' % avg

avg = ( d1 + d2 ) / ( t1 + t2 ) * 60 * mtok
print 'the average speed for both rides in kilometers per hour is %5.2f' % avg
