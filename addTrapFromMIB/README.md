<b>[Description]</b>

	Adds new EventClassMapping Instances on ZenOSS from a MIB file. Permits extract SNMP TRAPs from a vendor MIB file and import to ZenOSS.

<b>[Usage]</b>

	TrapToEventClassMapping.py  [/path/to/MIBfilename] [prefix]
	
	[prefix] : Solve the ZenOSS problem if two Trap have a same name into the ZenOSS. You can type the prefix than you want apply before Trap name to relabel the original trap name into the ZenOSS system.
	

<b>[Example Usage]</b>

	TrapToEventClassMapping.py ./CISCO-TRAP-MIB.my CSCO