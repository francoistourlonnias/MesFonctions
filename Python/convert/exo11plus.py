# -*- encoding: utf8 -*-

note=20.0
lnotes=[]
somme=0.0

while float(note) >= 0:
	print("entrez une note, val negative pour sortir")
	a=float(input())
	#print("===>",a)
	if a < 0.0:
		exit(0)
	else:
		lnotes.append(a)
		idx=len(lnotes)
		print("nombres de notes: ",idx)
		note=float(lnotes[(idx-1)])

	
	print("liste des notes saisies ",lnotes)
	print("la note maxi ",max(lnotes))
	print("la note mini ",min(lnotes))
	
	print("lnotes :",lnotes)
	somme=0.0
	for i in lnotes:
		print("==>",i)
		somme+=i
		print("somme ",somme)
	moy=somme/idx
	print("moyenne",moy)
	
