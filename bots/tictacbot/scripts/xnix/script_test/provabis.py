#!/usr/bin/python3

import sys
#import json

#nome_utente=sys.argv[1]
#
#data={nome_utente:[{'name':'name'}]}

#jsdb=json.dumps(data, indent=4)

f=open("testbis.txt","r")
#out_file.write("Ecco qua\n")
#out_file.write(jsdb)
for line in f.readlines():
	sys.stdout.write(line)
f.close()

