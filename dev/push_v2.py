import json
import yaml
import time

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
			with open(config_file, 'r') as secret:
				config = json.load(secret)
		except json.decoder.JSONDecodeError:
			print('Error: Unable-To-Load-Config: ' + config_file)
			time.sleep(5)
			sys.exit(1)
	elif os.path.isfile('secret.yml'):
		config_file = 'secret.yml'
		try:
			with open(config_file, 'r') as secret:
				config = yaml.safe_load(secret)
		except yaml.scanner.ScannerError:
			print('Error: Unable-To-Load-Config: ' + config_file)
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
		time.sleep(5)
		sys.exit(1)

	try:
		config['credential']['endpoint']
	except NameError:
		print('Error: Unable-To-Load-Config: ' + config_file)
		time.sleep(5)
		sys.exit(1)
	except KeyError:
		print('Error: Unable-To-Load-Config: ' + config_file)
		time.sleep(5)
		sys.exit(1)
		
	api_url = config['credential']['endpoint']
	
	
	
	# Phrase
	phrase_raw = ''
	phrase_arr = [[]]
	phrase_file = 'phrase.json'
	if False :
		pass
	elif os.path.isfile('phrase.json'):
		phrase_file = 'phrase.json'
		try:
			with open(phrase_file, 'r') as phrase:
				phrase_arr = json.load(phrase)
		except json.decoder.JSONDecodeError:
			print('Error: Unable-To-Load-Phrase: ' + phrase_file)
			print('\t', end='')
			time.sleep(5)
			sys.exit(1)
	else:
		print('Error: No-Such-File-Or-Directory: phrase.json')
		print('Hint: Require phrase file(phrase.json)')
		print('Hint: Making a phrase file... ')
		try:
			phrase_raw = json.dumps(phrase_arr)
			with open(phrase_file, 'w') as phrase:
				phrase.write(phrase_raw)
		except json.decoder.JSONDecodeError:
			print('Error: Unable-To-Write-File: ' + phrase_file)
			print('\t', end='')
			print('Encode error')
			time.sleep(5)
			sys.exit(1)
		except:
			print('Error: Unable-To-Write-File: ' + phrase_file)
			print('\t', end='')
			print('Unkown error')
			time.sleep(5)
			sys.exit(1)

		time.sleep(5)
		sys.exit(1)

	msg_text = ''
	msg_text += '\n'

	arr_text = []


main()