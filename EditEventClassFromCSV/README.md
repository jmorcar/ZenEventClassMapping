<b>[Description]</b>

	Edit/Modify EventClassMapping Instances on ZenOSS from a CSV. Permits edit python transforms indicating severity of event in massive list of event class mappings.

<b>[Usage]</b>

	EditEventClassFromCsv.py  [/path/to/CSVfile] [prefix]
	
	[prefix] : Solve the ZenOSS problem if two Trap have a same name into the ZenOSS. You can type the prefix than you want apply before Trap name to relabel the original trap name into the ZenOSS system.
	

<b>[Example Usage]</b>

	TrapToEventClassMapping.py ./CISCO-TRAP-MIB.my CSCO