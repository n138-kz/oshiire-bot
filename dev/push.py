import requests
import json
import random
import datetime
import os
import sys
import yaml

# refs docs: https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
# refs docs: https://discord.com/channels/394476575581798400/1079832126142296144/1079846440349741077

config = { 'credential': 'endpoint': '' }
if not os.path.isfile('config.yml'):
    with open('config.yml', 'w') as yml:
        yaml.dump(config, yml)
    sys.exit(1)

with open('config.yml', 'r') as yml:
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

msg_text += '[原神 (Genshin Impact)]\n'
msg_text += '[act.hoyolab.com](https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&lang=ja-jp)\n'

payload2 = {
    "payload_json" : {
        "content" : "",
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
