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

    arr_text = []

    arr_text.append(
        ''
        + 'にぃにとねぇね、デイリーログイン報酬は受け取りましたか〜？\n'
        + 'よしよし，ちゃんと忘れないように、教えてあげますからね〜\n'
        + '\n'
    ) # Yaoyao
    arr_text.append(
        ''
        + 'ふふん…栄誉騎士、クレーは「火花騎士」として西風騎士団の先輩なんだよ？\n'
        + 'だからね！だから…クレーが起こしたトラブル、内緒にしてくれないかな…\n'
        + '\n'
    ) # Klee
    arr_text.append(
        ''
        + 'まだログボ受け取ってないとか言わないよね？\n'
        + 'この僕が知らせてるんだ、もちろん受け取ってるよね？\n'
        + 'あらら〜まだ受け取ってないの〜？へなちょこめ〜\n'
        + '\n'
    ) # Scaramouche
    arr_text.append(
        ''
        + '相棒！ログボは受け取った？早くしないと無くなっちゃうよ〜？\n'
        + '事件の予感がする…！ログボを受け取るのは君に任せたよ！\n'
        + '\n'
    ) # Heizo Shikanoin
    arr_text.append(
        ''
        + '旅人じゃないか、お前も1杯飲みに来たか？…そうか、違うのか。まぁ今度時間がある時にでも飲もう。あぁそうだ、悪いことは言わない、ログインボーナスは受け取って行けよ。\n'
        + '\n'
    ) # Kaeya
    arr_text.append(
        ''
        + 'あっ旅人さん、奇遇ですね。えっとその、これ…私からのプレゼントです。受け取って下さいますか？\n'
        + '\n'
    ) # Ayaka Kamisato
    arr_text.append(
        ''
        + '丁度いいところに！お嬢がそわそわしたまま旅人の事探してたから、時間があったら神里屋敷に寄って行かないか？もちろんおもてなしさせてもらうよ\n'
        + '\n'
    ) # Thoma

    msg_text += arr_text[random.randint(0,(len(arr_text)-1))]

    msg_text += 'https://webstatic.hoyoverse.com/upload/op-public/2023/03/29/46662c4742b02e88e218384adf395f3b_8860534905048955210.jpg'

    for i in range(5):
        msg_text += '\n'

    payload2 = {
        "payload_json" : {
            'username': 'みんなのまま',
            'content' : 'here ',
            "embeds": [
                {
                    "description"   : msg_text,
                    "url"           : "https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&lang=ja-jp\n",
                    "color"         : 5620992,
                    "timestamp"     : datetime.datetime.now().isoformat(),
                    "image": {
                        "url"       : "attachment://images_001.png"
                    },
                    "footer": {
                        'text'      : 'Version: ' + '3.5'
                                    + '#' + str( math.floor( os.path.getmtime( __file__ ) ) ) + '\n',
                    },
                    "fields": [
                        {
                            'inline': False,
                            'name'  : "原神 (Genshin Impact)",
                            'value' : "- [HoYoLAB: Daily Bounus](https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&lang=ja-jp)\n"
                                    + '- [Ver.3.5公式PV](https://youtu.be/M6g20c4a8Q4)'
                                    + '',
                        },
                        {
                            'inline': False,
                            'name'  : "HoYoLAB × Prime Gaming",
                            'value' : '- [HoYoLAB: 原神(Genshin)公式](http://hoyo.link/1eyUCEAd)\n'
                                    + '- [Prime Gaming: 原神コラム#6](https://gaming.amazon.com/genshin-impact-6?ref_=SM_GI02_P6_IGP)\n'
                                    + 'Until: 4月19日 24:59 (JST)\n',
                        },
                        {
                            'inline': False,
                            'name'  : "予告番組最新情報",
                            'value' : '- [HoYoLAB: Ver.3.6](https://genshin.hoyoverse.com/ja/news/detail/110865)\n'
                                    + '- [Youtube](https://youtu.be/uda3T168Wpg)\n'
                                    + '- [bilibili](http://live.bilibili.com/21987615)\n'
                                    + '- [twitch](https://www.twitch.tv/genshinimpactofficial)\n'
                                    + 'Time: 3月31日(金) 21:00 (JST)\n',
                        },
                        {
                            'inline': False,
                            'name'  : '',
                            'value' : '',
                        },
                        {
                            'inline': True,
                            'name'  : '( ๑╹⌓╹ )',
                            'value' : '[' + 'DevOps Server' + '](' + 'https://discord.gg/9Y5TXp2Rx2' + ')\n'
                                    + '[' + 'Build Status' + '](https://github.com/n138-kz/oshiire-bot/actions/workflows/Docker-test_dev.yml)\n'
                                    + '',
                        },
                        {
                            'inline': True,
                            'name'  : 'ヾ(๑╹◡╹)ﾉ"',
                            'value' : '(๑•̀ㅂ•́)و✧\n'
                                    + '(๑•̀ㅂ•́)و✧\n'
                                    + '(๑•̀ㅂ•́)و✧\n'
                                    + '',
                        },
                        {
                            'inline': False,
                            'name'  : '',
                            'value' : '',
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

