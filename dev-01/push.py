import requests
import json
import random
import datetime
import os
import sys
import yaml
import math

# refs docs: https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
# refs docs: https://qiita.com/ABBBB/items/e6bdf7fc94b8f6f72a01

def md5calc(file):
    import hashlib
    with open(file, 'rb') as fp:
        fileData = fp.read()
        hash = hashlib.md5(fileData).hexdigest()
    return hash

def main():
    config = { 'credential': { 'endpoint': '' } }
    if not os.path.isfile('secret.yml'):
        print('Error: NoSuchFileOrDirectory: secret.yml')
        with open('secret.yml', 'w') as yml:
            yaml.dump(config, yml)
        sys.exit(1)

    with open('secret.yml', 'r') as yml:
        config = yaml.safe_load(yml)
        
    api_url = config['credential']['endpoint']

    msg_text = ''
    msg_text += '\n'

    msg_text += '-----\n'

    for i in range(5):
        msg_text += '\n'

    # https://qiita.com/GrapeColor/items/bdcf8431b13091447028
    payload2 = {
        "embeds": [
            {
                "url": "https://twitter.com/GrapeColorSoft/status/1205289368786620416",
                "description": "複数枚画像投稿テスト",
                "author": {
                "name": "GrapeColor (@GrapeColorSoft)",
                "url": "https://twitter.com/GrapeColorSoft",
                "icon_url": "https://pbs.twimg.com/profile_images/1063236006135062528/493Dm2lD_bigger.jpg"
            },
                "image": {"url": "https://pbs.twimg.com/media/ELoMRwLVUAAFlm_.jpg:large"}
            },
            {
                "url": "https://twitter.com/GrapeColorSoft/status/1205289368786620416",
                "image": {"url": "https://pbs.twimg.com/media/ELoMRwNU8AEMaoO.jpg:large"}
            },
            {
                "url": "https://twitter.com/GrapeColorSoft/status/1205289368786620416",
                "image": {"url": "https://pbs.twimg.com/media/ELoMRwNUwAAWako.jpg:large"}
            },
            {
                "url": "https://twitter.com/GrapeColorSoft/status/1205289368786620416",
                "image": {"url": "https://pbs.twimg.com/media/ELoMRwMU8AELiyj.jpg:large"}
            }
        ]
    }



    payload2['embeds'] = json.dumps( payload2['embeds'], ensure_ascii=False )
    curl_res = requests.post(api_url, data = payload2 )
    #print(curl_res.status_code) # HTTPのステータスコード取得
    #print(curl_res.text)        # レスポンスのHTMLを文字列で取得

    if(False):
        pass
    elif( curl_res.status_code >= 200 and curl_res.status_code < 300 ):
        # OK
        print( json.dumps( json.loads( curl_res.text ), indent=4, separators=(',', ': '), ensure_ascii=False ) )
    elif( curl_res.status_code >= 300 and curl_res.status_code < 400 ):
        # Redirected
        print( curl_res.status_code )
    elif( curl_res.status_code >= 400 ):
        # All errors
        print( curl_res.status_code)
        print( curl_res.text)
    elif( curl_res.status_code >= 400 and curl_res.status_code < 500 ):
        # Client errors
        pass
    elif( curl_res.status_code >= 500 ):
        # Server errors
        pass

    return curl_res

def test_main():
    main()

main_result = main()
if(False):
    pass
elif( main_result.status_code < 400 ):
    sys.exit(0)
else:
    sys.exit(1)

