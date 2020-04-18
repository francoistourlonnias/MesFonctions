from datetime import date      

print "Content-type: text/html"



print """

<html>

   <body>
      <h1>Today's date is 
"""        
today = date.today()
print today

print """    

    </h1>
   
   </body>


</html>

"""
