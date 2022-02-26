from flask import Flask, request
from urllib.parse import unquote
import translators as ts
app = Flask(__name__)

translated_list = {}
converted_list = {}

@app.route("/translate/")
def trans():
	text = unquote(request.args.get('text')).strip().lower()
	if text in translated_list:
		return {'text': translated_list[text]['text'], 'lang': translated_list[text]['lang']}
	else:
		data = ts.google(text, is_detail_result=True)
		textTranslated = data[1][0][0][5][0][0] or data[1][0][0][5][0][4][0][0]
		lang = data[2]
		if textTranslated:
			translated_list[text] = {'text': textTranslated, 'lang': lang}
			return {'text': textTranslated, 'lang': lang}
		else:
			return ''

@app.route("/translateto/")
def transto():
	text = unquote(request.args.get('text')).strip().lower()
	lang = unquote(request.args.get('lang')).strip().lower()
	if '%s_%s' %(text,lang) in converted_list:
		return converted_list['%s_%s' %(text,lang)]
	else:
		if lang:
			textTranslated = ts.google(text, 'auto', lang)
			converted_list['%s_%s' %(text,lang)] = textTranslated
			return {'text': textTranslated}
		else:
			return ''

@app.route('/')
def index():
	return 'use either translate or translateto'
