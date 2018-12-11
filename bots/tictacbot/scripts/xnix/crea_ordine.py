#!/usr/bin/python3
import sys
import json
import os
import time

cognome=sys.argv[1]
nome=sys.argv[2]
modello=sys.argv[3]
colore_cinturino=sys.argv[4]
vetrino_sino=sys.argv[5]
indirizzo=sys.argv[6]
città=sys.argv[7]
cap=sys.argv[8]
cellulare=sys.argv[9]
prezzo=sys.argv[10]
carta=sys.argv[11]

ora=time.strftime("%H")
minuto=time.strftime("%M")
secondo=time.strftime("%S")
giorno=time.strftime("%d")
mese=time.strftime("%m")
anno=time.strftime("%Y")

cellulare=cellulare.replace(' ','')
prezzo=prezzo.replace(' ','')
carta=carta.replace(' ','')
giorno_ordine=giorno+"/"+mese+"/"+anno
orario_ordine=ora+":"+minuto+":"+secondo
id_ordine=anno[2:]+mese+giorno+nome[1:3]+cognome[1:3]+ora+minuto+secondo
id_ordine=id_ordine.upper()

if vetrino_sino == " hai ":
	vetrino_sino="si"
if vetrino_sino == " non hai ":
	vetrino_sino="no" 

ordine={id_ordine:[{
'cognome':cognome,
'nome':nome,
'cellulare':cellulare,
'modello':modello,
'colore_cinturino':colore_cinturino,
'ha_aggiunto_vetrino':vetrino_sino,
'indirizzo':indirizzo,
'citta':città,
'cap':cap,
'prezzo':prezzo,
'carta':carta,
'giorno':giorno_ordine,
'orario':orario_ordine
} ]}

jsdb=json.dumps(ordine, indent=4)

os.chdir('../../ordini')
file_path=id_ordine+".json"

out_file=open(file_path,"w")
out_file.write(jsdb)
out_file.close()

print(id_ordine)
