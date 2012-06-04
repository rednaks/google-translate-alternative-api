#!/usr/bin/python
#-*- coding: utf-8 -*-

from  mods.AlternativeApi import *
import cgi




form = cgi.FieldStorage()        
print 'Content-type: text/html'
print 

#print '<html><body>'
get_data = form.getvalue('text')
json = form.getvalue('json')
if(get_data is not None):
	my_page = curl(cgi.escape(form.getvalue('text')))
	#print 'Translating ...'
	parser = MyHTMLParser()
	parser.feed(my_page)
	#print '<p> Text to translate : '+get_data+'</p>'
	my_text = parser.text;
	print parser
	if(json == 'true'):
		my_text = '{"source": "%s", "translated": "%s"}' %(get_data,my_text)

	print my_text,
	#print '<p> text: '+cgi.escape(form.getvalue('text'))+'</p>'
else:
	print '''
			<h1> 404 not found !</h1>
			<p> seriously ? :D try with rednaks.alwaysdata.net/translate/?text=&lt;text to translate&gt;</p>
			<p> To get json format add json=true option</p>'''
#print '</body></html>'




