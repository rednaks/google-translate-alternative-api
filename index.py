#!/usr/bin/python
#-*- coding: utf-8 -*-

import pycurl
import urllib
import StringIO
from lib.HTMLParser import HTMLParser
import cgi



found = False
my_text = ''
    
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global found
        try:
            if(attrs[0] == ('id','result_box')): 
                found = True             
        except:
            i=1 # Nothing to do, so i = 1 :D
            
    def handle_endtag(self, tag):
        global found
        if(tag == 'div'):
            found = False
            
    def handle_data(self, data):
        global found
        global my_text
        if(found):
         my_text = my_text+ data


def curl(text):
	URL = 'http://translate.google.com/'
	#dataToTranslate = "Простой и лаконичный интерфейс позволяет освоить программу за несколько минут. Безопасность, высокая скорость работы, гибкость и расширяемость — основные качества, присущие Mozilla Firefox"
	data = {'sl':'auto','tl':'en','js':'n','prev':'_t','hl':'en','ie':'UTF-8','layout':'2','eotf':'1','text':text,'file':''}
	handle = pycurl.Curl()
	b = StringIO.StringIO()
	handle.setopt(pycurl.URL,URL)
	handle.setopt(pycurl.POST,1)
	handle.setopt(pycurl.POSTFIELDS,urllib.urlencode(data))
	handle.setopt(pycurl.WRITEFUNCTION,b.write)
	handle.perform()
	return b.getvalue()


form = cgi.FieldStorage()        
print 'Content-type: text/html'
print 

#print '<html><body>'
get_data = form.getvalue('text')
if(get_data is not None):
	my_page = curl(cgi.escape(form.getvalue('text')))
#	print 'Translating ...'
	parser = MyHTMLParser()
	parser.feed(my_page)
#	print '<p> Text to translate : '+get_data+'</p>'
	print my_text
	#print '<p> text: '+cgi.escape(form.getvalue('text'))+'</p>'
else:
	print '''
			<h1> 404 not found !</h1>
			<p> seriously ? :D try with rednaks.alwaysdata.net/translate/?text=&lt;text to translate&gt;</p>'''
#print '</body></html>'




