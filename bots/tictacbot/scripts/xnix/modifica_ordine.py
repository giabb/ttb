#!/usr/bin/python3

import sys
import os
import json
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
id_ordine=sys.argv[10]
prezzo=sys.argv[11]
carta=sys.argv[12]

id_ordine=id_ordine.replace(' ','')
cellulare=cellulare.replace(' ','')
prezzo=prezzo.replace(' ','')
carta=carta.replace(' ','')
vetrino_sino=vetrino_sino.replace(' ','')

anno=id_ordine[:2]
mese=id_ordine[2:4]
giorno=id_ordine[4:6]
ora=id_ordine[10:12]
minuto=id_ordine[12:14]
secondo=id_ordine[14:16]

ora_mod=time.strftime("%H")
minuto_mod=time.strftime("%M")
secondo_mod=time.strftime("%S")
giorno_mod=time.strftime("%d")
mese_mod=time.strftime("%m")
anno_mod=time.strftime("%Y")

giorno_ordine=giorno+"/"+mese+"/20"+anno
giorno_ordine_mod=giorno_mod+"/"+mese_mod+"/"+anno_mod

orario_ordine=ora+":"+minuto+":"+secondo
orario_ordine_mod=ora_mod+":"+minuto_mod+":"+secondo_mod

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
'orario':orario_ordine,
'giorno_modifica':giorno_ordine_mod,
'orario_modifica':orario_ordine_mod
} ]}

jsdb=json.dumps(ordine, indent=4)

os.chdir('../../ordini')
file_path=id_ordine+".json"

out_file=open(file_path,"w")
out_file.write(jsdb)
out_file.close()

print("L'ordine")
print(id_ordine)
print("è stato modificato con successo")
