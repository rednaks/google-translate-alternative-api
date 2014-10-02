
#-*- coding: utf-8 -*-

import requests
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
import re

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

def BeautifulParser(page):
	translated_text = ''
	soup = BeautifulSoup(str(BeautifulSoup(page).findAll(id='result_box')[0]))
	i = 0
	for s in soup.findAll('span'):
		if(i is not 0):
			translated_text += s.getText()+' '
		i += 1

	return translated_text
	 
		


def curl(text):
	URL = 'https://translate.google.com/'
	data = {'sl':'auto','tl':'en','js':'n','hl':'en','ie':'UTF-8','text':text,'file':''}
	res = requests.post(URL, data)
	if(res.ok):
		return res.content
	return None

