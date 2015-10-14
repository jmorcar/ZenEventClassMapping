<b>[Description]</b>

	Adds new EventClassMapping Instances on ZenOSS from a MIB file. Permits extract SNMP TRAPs from a vendor MIB file and import to ZenOSS.

<b>[Usage]</b>

	1- addTrapFromMIB.py [/path/to/MIBfilename] [prefix]  - Add Traps to ZenOSS MIB database like zenmib, because uses zenmib command to updoad the MIB file.
	2- TrapToEventClassMapping.py  [/path/to/MIBfilename] [prefix] - Adds the Traps of a MIB to Event Mapping Zenoss database to handle events, their transforms, rules....
	
	[prefix] : Defaul is empty. Solve the ZenOSS problem if two Trap have a same name into the ZenOSS. You can type the prefix than you want apply before Trap name to relabel the original trap name into the ZenOSS system.
	

<b>[Example Usage]</b>

	1- To add in Zenoss MIB zodb, with CSCO prefix (All trap name will be rename at the beginning: CSCO<trapname> : 
		# addTrapFromMIB.py /path/to/CISCO-TRAP-MIB.my CSCO
	2- To add in Zenoss Event Mapping zodb: 
		#TrapToEventClassMapping.py /path/to/CISCO-TRAP-MIB.my CSCO