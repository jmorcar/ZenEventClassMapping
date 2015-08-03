[Description]
	Adds new EventClassMapping Instances on ZenOSS from a CSV file.

[Usage]
	add_EventClassMapping_from_csv.py  [path/to/CSV_file_name]

[CSV Format]

	Trapname;Trap_OID;Category;N/A;Severity;Message

[Example]

	communicationLost;.1.3.6.1.4.1.318.0.1;Energia;2;Minor;comunicacion perdida;;;;;;;;;;;;;;;;;;;;;;;


[Note]
	* Category : You can type "LOGONLY" category to send this Trap directly to History Zenoss Event console. Any another Category name only adds this Trap to Status Event console.
	* N/A: For future implementations. This field is not supported yet.
	* Severity: You can type the severity name what you want in ZenOSS. The Severity is inserted as a new pyhton Transform of this EventClassMapping.