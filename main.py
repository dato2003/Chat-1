from flask import *
import os
import time
from datetime import datetime
import requests
import json
import base64
import random
import lib
from OpenSSL import SSL
context = ('Keys/ssl.crt', 'Keys/ssl.key')
app = Flask(__name__)
app.config.from_object('config')





@app.route('/lib/send/<string:message>/<string:token>')
def send_message(message,author):
	lib.database.new_message(message,author)
	return ""
@app.route('/lib/user/create/<string:username>/<string:password>')
def create_user(username,password):
	lib.database.new_user(username,password,0)
	return ""
@app.route('/lib/info/<int:user>')
def user_info(user):
	return str(lib.database.lookup_user(user))

@app.route('/lib/messages')
def get_messages():
	return str(lib.database.get_messages())
@app.route("/lib/tests/lib/<string:uname>")
def test_userInfo(uname):
	pass




















@app.route('/<path:page>')
def loadHtml(page):
	try:
		f = open("lib/gui/"+page+".html")
		res = f.read()
		f.close()
		return res
	except:
		f = open("lib/gui/404.html")
		res = f.read()
		f.close()
		return res






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'),ssl_context=context)	