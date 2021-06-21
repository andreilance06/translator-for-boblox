from flask import Flask, request
from urllib.parse import unquote
import translators as ts
app = Flask(__name__)

@app.route("/translate/")
def trans():
	text = unquote(request.args.get('text'))
	textTranslated = ts.google(text, is_detail_result=True)
	if textTranslated:
		return textTranslated
	else:
		return ''

@app.route("/translateto/")
def transto():
	text = unquote(request.args.get('text'))
	lang = unquote(request.args.get('lang'))
	if lang:
		textTranslated = ts.google(text, 'auto', lang, is_detail_result=True)
		return textTranslated
	else:
		return ''

@app.route('/')
def index():
	return 'use either translate or translateto'