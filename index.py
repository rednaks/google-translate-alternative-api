#!/usr/bin/python
#-*- coding: utf-8 -*-

from  mods.AlternativeApi import *

from flask import Flask, render_template, request, jsonify, abort



app = Flask(__name__)



@app.route('/api/v1/', methods=['GET'])
def translate():
  text = ''
  text = request.args['text']

  page = curl(text)
  tr_text = BeautifulParser(page)
  if(len(tr_text) == 0):
    return abort(503)

  return jsonify({'original':text,'translated':tr_text})



@app.route('/')
def index():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')
