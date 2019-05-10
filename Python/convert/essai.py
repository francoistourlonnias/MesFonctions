def dechex(deci):
    def quinze(nb):
        base = 16
        div=nb
        while res != 0:
        	res=base/div
        	r=base%div
        	print (res,r)
        	div=res
 
        return r
        
    if deci <= 15:
        return quinze(deci)
    else:
        print("trop grand") 
        
print (dechex(5))