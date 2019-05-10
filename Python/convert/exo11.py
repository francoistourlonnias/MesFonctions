# -*- encoding: utf8 -*-

note=20.0
lnotes=[]

while float(note) >= 0:
	print("entrez une note, val negative pour sortir")
	lnotes.append(input())
	idx=len(lnotes)
	print("nombres de notes: ",idx)
	note=float(lnotes[(idx-1)])
	if note <0:
		exit(0)
	
	print(lnotes)
	
print(lnotes)