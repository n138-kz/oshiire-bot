import os
import sys
import json
import yaml
import time
import sqlite3
import random
import datetime
import math
import zlib

def md5calc(file):
	import hashlib
	with open(file, 'rb') as fp:
		fileData = fp.read()
		hash = hashlib.md5(fileData).hexdigest()
	return hash

def main():
	# Config
	config = { 'credential': { 'endpoint': '' } }
	config_file = ''
	if False :
		pass
	elif os.path.isfile('secret.json'):
		config_file = 'secret.json'
		try:
			with open(config_file, 'r', encoding='utf-8') as secret:
				config = json.load(secret)
		except json.decoder.JSONDecodeError:
			print('Error: Unable-To-Load-Config: ' + config_file)
			print('exit...')
			time.sleep(5)
			sys.exit(1)
	elif os.path.isfile('secret.yml'):
		config_file = 'secret.yml'
		try:
			with open(config_file, 'r', encoding='utf-8') as secret:
				config = yaml.safe_load(secret)
		except yaml.scanner.ScannerError:
			print('Error: Unable-To-Load-Config: ' + config_file)
			print('exit...')
			time.sleep(5)
			sys.exit(1)
	else:
		print('Error: NoSuchFileOrDirectory: secret.json, secret.yml')
		print('Hint: Require config file(secret.json or secret.yml)')
		print('Hint: Load priority: ')
		print('\t', end='')
		print('1. secret.json')
		print('\t', end='')
		print('2. secret.yml')
		print('exit...')
		time.sleep(5)
		sys.exit(1)

	try:
		config['credential']['endpoint']
	except NameError:
		print('Error: Unable-To-Load-Config: ' + config_file)
		print('exit...')
		time.sleep(5)
		sys.exit(1)
	except KeyError:
		print('Error: Unable-To-Load-Config: ' + config_file)
		print('exit...')
		time.sleep(5)
		sys.exit(1)
		
	api_url = config['credential']['endpoint']
	
	
	
	# Phrase
	phrase_raw = ''
	phrase_arr = [['']]
	phrase_file = 'phrase.json'
	if False :
		pass
	elif os.path.isfile('phrase.json'):
		phrase_file = 'phrase.json'
		try:
			with open(phrase_file, 'r', encoding='utf-8') as phrase:
				phrase_arr = json.load(phrase)
		except json.decoder.JSONDecodeError:
			print('Error: Unable-To-Load-Phrase: ' + phrase_file)
			print('\t', end='')
			print('exit...')
			time.sleep(5)
			sys.exit(1)
	else:
		print('Error: No-Such-File-Or-Directory: phrase.json')
		print('Hint: Require phrase file(phrase.json)')
		print('Hint: Making a phrase file... ')
		try:
			phrase_raw = json.dumps(phrase_arr)
			with open(phrase_file, 'w', encoding='utf-8') as phrase:
				phrase.write(phrase_raw)
		except json.decoder.JSONDecodeError:
			print('Error: Unable-To-Write-File: ' + phrase_file)
			print('\t', end='')
			print('Encode error')
			print('exit...')
			time.sleep(5)
			sys.exit(1)
		except:
			print('Error: Unable-To-Write-File: ' + phrase_file)
			print('\t', end='')
			print('Unkown error')
			print('exit...')
			time.sleep(5)
			sys.exit(1)

		if os.path.isfile('phrase.json'):
			print('Info: Succeed-Create-File: ' + phrase_file)
		else:
			print('Error: Unable-To-Create-File: ' + phrase_file)
		
		print('exit...')
		time.sleep(5)
		sys.exit(1)
	
	
	
	# sqlite3
	database_file = 'result.db'
	database_dsn = sqlite3.connect(database_file)
	
	database_cur = database_dsn.cursor()
	try:
		database_cur.execute('CREATE TABLE runResult(iat INTEGER PRIMARY KEY, detail STRING)')
		database_dsn.commit()
		
		print('Info: Initilized database: ' + database_file)
		print('\t', end='')
		print('exit...')
		
		time.sleep(5)
		sys.exit(1)
	except sqlite3.OperationalError as e:
		pass
	database_dsn.close()
	
	
	
	# main()
	print('Debug: main()')
	
	msg_text = ''
	msg_text += '\n'

	msg_text += phrase_arr[random.randint(0,(len(phrase_arr)-1))][0]
	msg_text += '～～～～～♪♫♪♫'

	for i in range(5):
		msg_text += '\n'



	# 発信情報
	payload = {
		"payload_json" : {
			'username': 'みんなのまま',
			'content' : chr(0),
			"avatar_url": "https://upload-os-bbs.hoyolab.com/upload/2022/11/24/21d71c44827fa664a6a21977d9a3dd1c_6799685155050732642.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png",
			"embeds": [],
		}
	}

	# メッセージ本体
	payload['payload_json']['embeds'].append(
		{
			'color': 0x3556ca,
			'timestamp': datetime.datetime.now().isoformat(),
			'footer': {
				'text': 'Version: ' + '4.3.0'
					+ '#' + str( hex( zlib.crc32( str( math.floor( os.path.getmtime( __file__ ) ) ).encode() ) )[2:] ) + '',
			},
			"fields": [
				{
					'inline': False,
					'name'  : "",
					'value' : msg_text,
				}
			],
		}
	)
	
	payload['payload_json']['embeds'][0]['fields'].append(
		{
			'inline': True,
			'name'  : "原神 (Genshin Impact)",
			'value' : ''
					+ ''
					+ '- [HoYoLAB: Daily Login Bounus](https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&lang=ja-jp)\n'
					+ '',
		},
	)
	
	payload['payload_json']['embeds'][0]['fields'].append(
		{
			'inline': False,
			'name'  : "",
			'value' : ''
					+ ''
					+ '- [Ver.4.3公式PV](https://youtu.be/l60SIb7ndso)\n'
					+ '- [Ver.4.3特設ページ](https://hoyo.link/2ztfFBAL)\n'
					+ '',
		},
	)
	
	payload['payload_json']['embeds'][0]['fields'].append(
		{
			'inline': False,
			'name'  : "",
			'value' : ''
					+ ''
					+ '- [Ver.4.2公式PV](https://youtu.be/gnG7XjEFnm4)\n'
					+ '- [Ver.4.2特設ページ](https://hoyo.link/0iyeFBAL)\n'
					+ '',
		},
	)
	
	payload['payload_json']['embeds'][0]['fields'].append(
		{
			'inline': False,
			'name'  : "",
			'value' : ''
					+ ''
					+ '- [Ver.4.1公式PV](https://www.youtube.com/watch?v=LsZx11uXVEw)\n'
					+ '- [Ver.4.1特設ページ](https://hoyo.link/azPeFHAL)\n'
					+ '',
		},
	)
	
	payload['payload_json']['embeds'][0]['fields'].append(
		{
			'inline': False,
			'name'  : "",
			'value' : ''
					+ ''
					+ '- [Ver.4.0公式PV](https://youtu.be/OlxaEK9K1Cs)\n'
					+ '- [Ver.4.0特設ページ](https://hoyo.link/1Ko9CBAL)\n'
					+ '',
		},
	)
	
	payload['payload_json']['embeds'][0]['fields'].append(
		{
			'inline': False,
			'name'  : "",
			'value' : ''
					+ ''
					+ '- [PS5 / PS4](https://www.playstation.com/ja-jp/games/genshin-impact/)\n'
					+ '- [Windows PC](https://sg-public-api.hoyoverse.com/event/download_porter/trace/ys_global/genshinimpactpc/default)\n'
					+ '- [Apple Store](https://apps.apple.com/app/id1517783697)\n'
					+ '- [Google Play](https://play.google.com/store/apps/details?id=com.miHoYo.GenshinImpact)\n'
					+ '- [Epicgames](https://www.epicgames.com/store/p/genshin-impact)\n'
					+ '',
		},
	)
	
	# 画像ファイル
	files_images = {}
	for i in range(10):
		file_name = 'images_{num}.png'
		file_name = file_name.replace('{num}', str(i+1).zfill(3))
		if os.path.isfile(file_name):
			with open(file_name, 'rb') as f:
				file_binary = f.read()
				files_images.update(
					{
						file_name: ( file_name, file_binary ),
					}
				)
			payload['payload_json']['embeds'].append(
				{
					'color': 0x3556ca,
					'url': 'https://twitter.com/Genshin_7',
					"image": {
						"url": 'attachment://' + file_name
					},
				},
			)


main()
