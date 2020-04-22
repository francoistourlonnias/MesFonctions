
# -*- encoding: utf-8 -*-
#decodage d'une trame NMEA
trame = "$GPGGA, 064036.289, 4836.5375, N, 00740. 9373, E, 1, 04, 3.2, 200.2, M, , , , 0000*0E"

#    GPGGA : type de la trame
#     064036.289 : heure d’envoi de la trame, ici 06h 40min 36,289s (UTC)
#     4836.5375, N : latitude Nord, ici 48°36,5375’ (en DM, degrés minutes)
#     00740.9373, E : longitude Est, ici 7°40,9373’ (en DM également)
#     1 : type de positionnement (1 pour le positionnement GPS)
#     04 : nombre de satellites utilisés
#     3.2 : précision horizontale
#     200.2, M : altitude, ici 200 mètres

#from gps import *

#fonction  qui renvoie le nom de l’équipement qui a émis la trame
def tramePrefixes(trame):
	talkerId=trame[1:3]
	if talkerId=="GD" or talkerId=="GB":
	   	tramePrefixesValue="Beidou"
	elif talkerId=="GA":
	    tramePrefixesValue="Galileo"
	elif talkerId=="GP":
	    tramePrefixesValue="GPS"
	elif talkerId=="GL":
	   	tramePrefixesValue="GLONASS"
	return tramePrefixesValue

# ggaUtc(trame) qui reçoit une trame complexe et renvoie l’heure en h, min, s.
def ggaUtc(trame):
    #on transforme la trame en liste
    attribut=trame.split(',')
    #on sélectionne l'élément qui correspond à l'heure
    time=attribut[1]
    utc=time[:2]+" h "+time[2:4]+" min "+time[4:]+" s"
    return utc

#fonction ggaLat(trame) qui reçoit une trame complète et renvoie la latitude convertie en DMS.
def ggaLat(trame):
	attribut=trame.split(',')
	lat=attribut[2]
	lat_deg=lat[:2]
	lat_min=lat[2:4]
	lat_sec=str(float(lat[4:])*60)
	latDMS=lat_deg+" D "+lat_min+" M "+lat_sec+" S "
	return latDMS


print (tramePrefixes(trame))
print (ggaUtc(trame))
print (ggaLat(trame))