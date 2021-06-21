from flask import Flask, request
from urllib.parse import unquote
import translators as ts
app = Flask(__name__)

@app.route("/translate/")
def trans():
	text = unquote(request.args.get('text'))
	data = ts.google(text, is_detail_result=True)
	textTranslated = data[1][0][0][5][0][0]
	lang = data[2]
	if textTranslated:
		return {'text': textTranslated, 'lang': lang}
	else:
		return ''

@app.route("/translateto/")
def transto():
	text = unquote(request.args.get('text'))
	lang = unquote(request.args.get('lang'))
	if lang:
		textTranslated = ts.google(text, 'auto', lang)
		return {'text': textTranslated}
	else:
		return ''

@app.route('/')
def index():
	return 'use either translate or translateto'