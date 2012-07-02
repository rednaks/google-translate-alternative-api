
#-*- coding: utf-8 -*-

import pycurl
import urllib
import StringIO
from lib.HTMLParser import HTMLParser

found = False
my_text = ''
    
class MyHTMLParser(HTMLParser):

#    def __init__(self):
#        self.text = ''


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
        if(found):
         self.text = self.text+ data


def curl(text,dlang='en'):
	URL = 'http://translate.google.com/'
	data = {'sl':'auto','tl':dlang,'js':'n','prev':'_t','hl':'en','ie':'UTF-8','layout':'2','eotf':'1','text':text,'file':''}
	handle = pycurl.Curl()
	b = StringIO.StringIO()
	handle.setopt(pycurl.URL,URL)
	handle.setopt(pycurl.POST,1)
	handle.setopt(pycurl.POSTFIELDS,urllib.urlencode(data))
	handle.setopt(pycurl.WRITEFUNCTION,b.write)
	handle.perform()
	return b.getvalue()

