#!/usr/bin/python3

import json
import sys
import os

id_ordine=sys.argv[1]
id_ordine_json=id_ordine+".json"

os.chdir('../../ordini')

with open(id_ordine_json,'r',encoding='utf-8') as jd:
	d = json.loads(jd.read())

#print(id_ordine)

carta=d[id_ordine][0]["carta"]
carta_cens=carta[0:1]+"***********"+carta[12:16]


print("COGNOME")
print(d[id_ordine][0]["cognome"])

print("NOME")
print(d[id_ordine][0]["nome"])

print("CELLULARE")
print(d[id_ordine][0]["cellulare"])

print("MODELLO")
print(d[id_ordine][0]["modello"])

print("COLORE CINTURINO")
print(d[id_ordine][0]["colore_cinturino"])

print("VETRINO")
print(d[id_ordine][0]["ha_aggiunto_vetrino"])

print("INDIRIZZO")
print(d[id_ordine][0]["indirizzo"])

print("CITTÀ")
print(d[id_ordine][0]["citta"])

print("CAP")
print(d[id_ordine][0]["cap"])

print("PREZZO")
print(d[id_ordine][0]["prezzo"])

print("CARTA")
print(d[id_ordine][0]["carta"])

print("CARTACENS")
print(carta_cens)
