#!/usr/bin/python
#-*- coding: utf-8 -*-

from  mods.AlternativeApi import *
import cgi




form = cgi.FieldStorage()        
print 'Content-type: text/html'
print 


get_data = form.getvalue('text')
json = form.getvalue('json')
lang_dest = form.getvalue('dlang')
if(get_data is not None):
	my_page = curl(cgi.escape(form.getvalue('text')),lang_dest)
	parser = MyHTMLParser()
	parser.feed(my_page)
	my_text = parser.text;
	if(json == 'true'):
		my_text = '{"source": "%s", "translated": "%s"}' %(get_data,my_text)

	print my_text,
else:
	print '''
			<h1> 404 not found !</h1>
			<p> seriously ? :D try with rednaks.alwaysdata.net/translate/?text=&lt;text to translate&gt;</p>
			<p> To get json format add json=true option</p>'''





