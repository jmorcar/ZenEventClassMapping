<b># Description</b>

	Adds new EventClassMapping Instances on ZenOSS from a python dictionary file.

<b># Usage</b>

	add_EventClassMapping.py  [path/to/CSV_file_name]

<b># Dictionary format</b>

	The format is:
	( #Beginning
	{ 'Trapname1'	: {	'severity':'Critical', 'transform' : 'Python code' , 'message' : 'N/S' , 'explanation' : "'Text to example and explanation field'" },
	  # You can add infinite lines 
	  # End line Trap hasn't the end "comma" character. 
	{ 'Trapname999'	: {	'severity':'Critical', 'transform' : 'Python code' , 'message' : 'N/S' , 'explanation' : "'Text to example and explanation field'" }
	}) #EndofFile

	^severity: The list of possible values and its ZenOSS conversion:
	'Clear': '0', 
	'Normal': '2',
	'Minor': '1',
    'Warning': '3',
	'Major': '4',
    'Critical': '5',
	
<b># Dictionary example</b>
	
	There is an example file on this project: datos_importacion.
	
	({ 'lowVoltTrap1'	: {	'severity':'Critical', 'transform' : 'if clear == 0: evt.severity = 5' , 'message' : 'evt.detalis.get(TrapString.0)' , 'explanation' : "'
	{ 'lowVoltTrap2'	: {	'severity':'Normal', 'transform' : 'if clear == 0: evt.severity = 5' , 'message' : 'evt.detalis.get(TrapString.0)' , 'explanation' : "'}
	{ 'lowVoltTrap3'	: {	'severity':'Warning', 'transform' : 'if clear == 0: evt.severity = 5' , 'message' : 'evt.detalis.get(TrapString.0)' , 'explanation' : "''" } })


<b># Note</b>

	* Category : You can type "LOGONLY" category to send this Trap directly to History Zenoss Event console. 
	Any another Category name only adds this Trap to Status Event console.
	* N/A: For future implementations. This field is not supported yet.
	* Severity: You can type the severity name what you want in ZenOSS. The Severity is inserted as a new pyhton Transform of this EventClassMapping.