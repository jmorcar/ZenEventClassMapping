#!/usr/bin/env python
import Globals, sys, ast, yaml, re
from transaction import commit
from Products.ZenUtils.ZenScriptBase import ZenScriptBase





if len(sys.argv) < 2:
     sys.exit('\nError faltan argumentos\n\nUsage: %s "fichero_CSV"\n\n' % sys.argv[0])



def evalSeverity(severity):
    return {
        'Clear': '1',
        'Normal': '2',
		'Warning': '2',
        'Minor': '3',
		'Major': '4',
        'Critical': '5',
    }.get(severity, 2)

def evalLogonly(logonly):
		if re.match("LOGONLY", logonly):
			return True
		else:
			return False


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
			


event_classes = '/Events/NUEVOS'
# PROVISION DE NUEVAS EVENTCLASSES EN ZENOSS
print "+ ADDING Event Class %s" % event_classes
conex = dmd.Events.getOrganizer('/')
conex.dmd.Events.manage_addOrganizer(event_classes)

	
	 
	 
#CARGAMOS EL FICHERO
file = sys.argv[1]	 
datos = open(file)
try:
		
        for line in datos:
				line_split = line.split(";" , 6)
				trap_name = line_split[0]
				oid = line_split[1]
				#print (line_split[2])
				logonly = evalLogonly(line_split[2])
				severidad = evalSeverity(line_split[4])
				texto_trap = line_split[5]
				mytransform = """ 
evt.severity = %s
evt.summary = '%s'
""" % (severidad , texto_trap)
				if logonly:
					mytransform += """
					
evt._action = "history"
"""
				
				print ("Editar instancia -> %s" % trap_name)
				#print (mytransform)
				org = dmd.Events.getOrganizer(event_classes)
				for i in org.find(trap_name):
						if i.eventClassKey == trap_name:
							inst = i
							inst.transform = mytransform
							for j in inst.sameKey():
								if inst.eventClassKey == j.eventClassKey:
									print("duplicado: %s" % j)
							
				
				
				
				
				#inst = org.find(trap_name)
				
				#print(inst)
				
				
				
				
				
#CERRAR FICHERO
finally:
        datos.close()	 
	 
	 


commit()
