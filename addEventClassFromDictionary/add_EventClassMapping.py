#!/usr/bin/env python
import Globals, sys, ast, yaml
from transaction import commit
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
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
event_classes = [
'/Events/NUEVOS'
]
filestr = '' #String para leer fichero de datos
#transformada de prueba
mytransform = """ 
datos=%s
evt.serverity = datos['severity']
evt.summary = datos['thr']
"""
definitions = [] 	#Array para importar a ZENOSS
###########################################

#LEER FICHERO DE DATOS TIPO DICTIONARY Y CONVERTIR A STRING
#datos = open("datos")
datos = open("datos_importacion")

try:
        for line in datos:
                filestr += line
#CERRAR FICHERO
finally:
        datos.close()

#CONVERTIR STRING DE DATOS A DICTIONARY

datosdict = ast.literal_eval(filestr)

# PROVISION DE NUEVAS EVENTCLASSES EN ZENOSS
print "+ ADDING Event Class "
conex = dmd.Events.getOrganizer('/')

for ec in event_classes:
       conex.dmd.Events.manage_addOrganizer(ec)

#for c, v in datosdict.items(): 
#	org = dmd.Events.getOrganizer('/Events/NUEVOS')
#	inst = org.createInstance('"' + c + '"')
#	inst.message = datosdict.get(c)['message']

for c, v in datosdict.items(): 
	org = dmd.Events.getOrganizer('/Events/NUEVOS')
	inst = org.createInstance(c)
	inst.eventClassKey = c
	inst.message = datosdict.get(c)['message']
#	inst.transform = 'evt.severity = ' + evalSeverity(datosdict.get(c)['severity'])
	inst.transform = datosdict.get(c)['transform']
        inst.explanation = datosdict.get(c)['explanation']
	inst.example = datosdict.get(c)['explanation']
	
	
	
#for definition in definitions:
#        org = dmd.Events.getOrganizer('/Events/NUEVOS')
#        inst = org.createInstance('"' + datosdict.values[definition]['name'] + '"')
#        inst.example = 'snmp trap ' + definition['name']
#        inst.transform = definition['transform']

# No /Events/Oracle needed, that is added automatically
# Sun HW Trap MIB - threshold notifications
#for sensor_short, sensor_type, zen_group in [
#        ('ShortPruebaVoltage', 'PruebaTypeVoltage', '/PruebaVoltage'),
#        ('ShortPruebaTemp', 'PruebaTemperature', '/PruebaTemperature')
#        ]:
#                for thr_value, severity, threshold_type in [
#                        ('Fatal', 5, 'non-recoverable'),
#                        ('Crit', 4, 'critical'),
#                        ('NonCrit', 3, 'non-critical')]:
#                                name = 'sunHwTrap' + sensor_short + thr_value + 'ThresholdExceeded'
#                                organizer = zen_group
#                                hw_thr_assert = None
#                                transform = mytransform % {
#                                                'severity':severity,
#                                                'thr':thr_value}
#                                d = {
#                                'name' : name,
#                                'organizer' : organizer,
#                                'transform' : transform}
#                                definitions.append(d)



commit()
