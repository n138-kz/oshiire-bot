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

    payload2 = {
        "payload_json" : {
            'username': 'みんなのまま',
            'content' : 'here ',
            "avatar_url": "https://upload-os-bbs.hoyolab.com/upload/2022/11/24/21d71c44827fa664a6a21977d9a3dd1c_6799685155050732642.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png",
            "embeds": [
                {
                    "description": "複数枚画像投稿テスト",
                    "author": {
                        "name": "みんなのまま",
                        "url": "https://twitter.com/GrapeColorSoft",
                        "icon_url": "https://pbs.twimg.com/profile_images/1063236006135062528/493Dm2lD_bigger.jpg",
                        "fields": [
                            {
                                'inline': False,
                                'name'  : '( ๑╹⌓╹ )',
                                'value' : '[' + 'DevOps Server' + '](' + 'https://discord.gg/9Y5TXp2Rx2' + ')\n'
                                        + '[' + 'Build Status (DEV)' + '](https://github.com/n138-kz/oshiire-bot/actions/workflows/Docker-test_dev.yml)\n'
                                        + '[' + 'Build Status (PRD)' + '](https://github.com/n138-kz/oshiire-bot/actions/workflows/Docker-test_prd.yml)\n'
                                        + '',
                            },
                        ],
                    },
                    "url": "https://twitter.com/GrapeColorSoft/status/1205289368786620416",
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
                },
                {
        
                },
            ],
        }
    }
    print(payload2['payload_json']['embeds'])

    # 画像ファイル
    files_images = {}
    for i in range(100):
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
            payload2['payload_json']['embeds'].append(
                { "color": 5620992, "image": {"url": 'attachment://' + file_name}, },
            )



    payload2['payload_json'] = json.dumps( payload2['payload_json'], ensure_ascii=False )
    curl_res = requests.post(api_url, files = files_images, data = payload2 )
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

