#!/usr/bin/env python

#==============================================================================
# title           : cadeado.py
# description     : AGI Cadeado para Asterisk
# author          : IPsafe - Henrique Chehad
# version         : 0.2
# usage           : Asterisk AGI
#==============================================================================


import sys,re
import MySQLdb


origem = sys.argv[1]
destino = sys.argv[2]

def hangup():
	print "EXEC PLAYBACK auth-incorrect \n"
	print "SET VARIABLE CDR(accountcode) \"Cadeado incorreto\""
	print 'HANGUP'
	sys.exit()


# Iniciando AGI
print "VERBOSE \"############# Iniciando Cadeado ############\" \n"

# Conexao MySQL
con = MySQLdb.connect(host='localhost', user='root', passwd='ipsafe',db='cadeado')
c = con.cursor()

# Consulta se o ramal esta com cadeado habilitado
c.execute("SELECT id FROM ramal WHERE ramal = '%s' AND NOT desabilitado " % origem)
res = c.fetchone()
if res:
	print "VERBOSE \"########### Cadeado Habilitado - %s ##########\"" % origem

	if destino[0] != '#' or len(destino) <= 7: 
		hangup()
		
	c.execute("SELECT id, nome FROM cadeado WHERE senha = '%s' AND NOT desabilitado " % destino[1:7])
	res = c.fetchone()
	if res:
		print "VERBOSE \"########### Cadeado Verificado - %s ##########\"" % origem
		print "SET VARIABLE CADEADO OK"
		print "SET VARIABLE CDR(accountcode) \"%s - %s\"" % (res[0], res[1])
		print "SET EXTENSION %s" % destino[7:]
	else:
		hangup()


else:
	# Cadeado desabilitado
	print "VERBOSE \"Cadeado Desabilitado\""
	print "SET VARIABLE CDR(accountcode) \"Cadeado desabilitado\""
	print "SET VARIABLE CADEADO OK"


