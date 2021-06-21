from flask import Flask, request
from urllib.parse import unquote
import translators as ts
app = Flask(__name__)

@app.route("/")
def trans():
	text = unquote(request.args.get('text'))
	textTranslated = ts.google(text)
	if textTranslated == text:
		return ''
	else:
		return textTranslated
