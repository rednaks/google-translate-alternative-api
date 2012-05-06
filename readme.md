This is an **alternative api** to google translate !


## TODO :

1. JSON, XML support.
2. This is translating form any language to English, so we would like to add other language support. 


## INSTALLING : 

* Make sure you have pycurl module installed.  
* Apache Configuration : 
To exacute python script you must add and .htaccess to your directory that will contain : 

		AddHandler cgi-script .py
		Options +ExecCGI
		DirectoryIndex index.py

* Test:
Now tape the url into the address bar of your favourite web browser and add ?text=<your text to translate> 
to get text translated in text format. if you want a JSON format you can add json=true in the url.

Enjoy ! 

## LICENSE	:
				DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
    	               Version 2, December 2004

		Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

		Everyone is permitted to copy and distribute verbatim or modified
		copies of this license document, and changing it is allowed as long
		as the name is changed.

				DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
		TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

		0. You just DO WHAT THE FUCK YOU WANT TO.


