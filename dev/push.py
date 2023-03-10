import requests
import json
import random
import datetime
import os
import sys
import yaml

# refs docs: https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
# refs docs: https://qiita.com/ABBBB/items/e6bdf7fc94b8f6f72a01

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

arr_text = []

arr_text.append(
	''
	+ 'にぃにとねぇね、デイリーログイン報酬は受け取りましたか〜？\n'
	+ 'よしよし，ちゃんと忘れないように、教えてあげますからね〜\n'
	+ '\n'
)
arr_text.append(
	''
	+ 'ふふん…栄誉騎士、クレーは「火花騎士」として西風騎士団の先輩なんだよ？\n'
	+ 'だからね！だから…クレーが起こしたトラブル、内緒にしてくれないかな…\n'
	+ '\n'
)

msg_text += arr_text[random.randint(0,(len(arr_text)-1))]

msg_text += '原神 (Genshin Impact)\n'
msg_text += '- [hoyolab daily login bounus](https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&lang=ja-jp)\n'

payload2 = {
    "payload_json" : {
        "username": "みんなのまま",
        "content" : "@here \<@768119883283169300>",
        "embeds": [
            {
                "description"   : msg_text,
                "url"           : "https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&lang=ja-jp\n",
                "color"         : 5620992,
                "timestamp"     : datetime.datetime.now().isoformat(),
                "image": {
                    "url"       : "attachment://images_001.png"
                },
                "fields": [
                    {
                        "name"  : "",
                        "value" : "",
                    },
                ],
            }
        ]
    }
}

### embed付き
with open("images_001.png", 'rb') as f:
    file_bin_logoeffect = f.read()
files_images  = {
    "logo_effect" : ( "images_001.png", file_bin_logoeffect ),
}

payload2['payload_json'] = json.dumps( payload2['payload_json'], ensure_ascii=False )
curl_res = requests.post(api_url, files = files_images  , data = payload2 )
print(curl_res.status_code) # HTTPのステータスコード取得
print(curl_res.text)        # レスポンスのHTMLを文字列で取得
