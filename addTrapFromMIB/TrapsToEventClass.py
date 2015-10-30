#!/usr/bin/env python





import Globals, sys, ast, yaml, os, tempfile
from transaction import commit
from Products.ZenUtils.ZenScriptBase import ZenScriptBase





if len(sys.argv) < 3:
     sys.exit('\nError faltan argumentos\n\nUsage: %s "fichero_MIBS" "cabecera_TRAPS"\n\n' % sys.argv[0])

file = sys.argv[1]
cabecera = sys.argv[2].upper()





#dmd = ZenScriptBase(connect=True).dmd
##########################################
# CONEXION CON ZOPE
conex = None
dmd = None
try:
    dmd = ZenScriptBase(connect=True).dmd
except Exception, e:
    print "Connection to zenoss dmd failed: %s\n" % e
    sys.exit(1)
###########################################

def evalSeverity(severity):
    return {
        'Clear': '0',
        'Normal': '2',
        'Minor': '1',
        'Warning': '3',
	'Major': '4',
        'Critical': '5',
    }.get(severity, 2)

#VARIABLES GLOBALES
#Definicion de Event Classes:  
# event_classes = [
#'/Events/clase1'
#'/Events/clase2'
#]

event_classes = '/Events/NUEVOS'

# PROVISION DE NUEVAS EVENTCLASSES EN ZENOSS
print "+ ADDING Event Class %s" % event_classes
conex = dmd.Events.getOrganizer('/')
conex.dmd.Events.manage_addOrganizer(event_classes)


#carga del fichero de mibs

filestr = '' #String para leer fichero de datos

definitions = [] 	#Array para importar a ZENOSS
###########################################

#EXTRAER LAS TRAPS DEL FICHERO DE MIB
outfile = tempfile.mkstemp(prefix="traps-out")
errfile = tempfile.mkstemp(prefix="traps-err")
os.system("smidump -c /etc/smi.conf --keep-going -f python %s > %s 2> %s " %  (file, outfile[1], errfile[1]))
errmsgs = open(errfile[1], "r").read()
os.unlink(errfile[1])
code = open(outfile[1],"r").read()
os.unlink(outfile[1])
try:
	exec(code)
except Exception, e:
	print >> sys.stderr, "%s - ha fallado la carga de la mib, %s" % (file, errmsgs)
	sys.exit(1)


try:
	traps = MIB['notifications']
except NameError:
	print >> sys.stderr, "%s was too badly formed to have output\n%s" % (file, errmsgs)
	sys.exit(1)
#print "traps: %s" % traps


for n , v in traps.items():
	nombre_trap = cabecera + n
	oid = traps.get(n)['oid']
	descripcion = traps.get(n)['description']
	varbinds = traps.get(n)['objects']
	descripcion += "\n Lista varbinds:"
	for o , b in varbinds.items():
		descripcion += "\n   %s" % o
	
	
	
	print ("Creando instancia -> %s" % nombre_trap)
	org = dmd.Events.getOrganizer(event_classes)
	inst = org.createInstance(nombre_trap)
	inst.example = descripcion
	inst.explanation = descripcion
	

commit()

	
	

	   


	
	
	








