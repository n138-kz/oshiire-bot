import requests
import json
import random
import datetime
import os
import sys
import yaml
import math
import zlib

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
    config_file = ''
    if False :
        pass
    elif os.path.isfile('secret.json'):
        config_file = 'secret.json'
        try:
            with open(config_file, 'r') as secret:
                config = json.load(secret)
        except json.decoder.JSONDecodeError:
            print('Error: UnableToLoadConfig: ' + config_file)
            sys.exit(1)
    elif os.path.isfile('secret.yml'):
        config_file = 'secret.yml'
        try:
            with open(config_file, 'r') as secret:
                config = yaml.safe_load(secret)
        except yaml.scanner.ScannerError:
            print('Error: UnableToLoadConfig: ' + config_file)
            sys.exit(1)
    else:
        print('Error: NoSuchFileOrDirectory: secret.json, secret.yml')
        print('Hint: Require config file(secret.json or secret.yml)')
        print('Hint: Load priority: ')
        print('   1. secret.json')
        print('   2. secret.yml')
        sys.exit(1)

    try:
        config['credential']['endpoint']
    except NameError:
        print('Error: UnableToLoadConfig: ' + config_file)
        sys.exit(1)
    except KeyError:
        print('Error: UnableToLoadConfig: ' + config_file)
        sys.exit(1)
        
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
        + '旅人じゃないか、お前も1杯飲みに来たか？\n'
        + '…そうか、違うのか。まぁ今度時間がある時にでも飲もう。\n\n'
        + 'あぁそうだ、悪いことは言わない、ログインボーナスは受け取って行けよ。\n'
        + '\n'
    ) # Kaeya
    arr_text.append(
        ''
        + 'あっ旅人さん、奇遇ですね。\n'
        + 'えっとその、これ…私からのプレゼントです。受け取って下さいますか？\n'
        + '\n'
    ) # Ayaka Kamisato
    arr_text.append(
        ''
        + '丁度いいところに！\n'
        + 'お嬢がそわそわしたまま旅人の事探してたから、時間があったら神里屋敷に寄って行かないか？\n'
        + 'もちろんおもてなしさせてもらうよ\n'
        + '\n'
    ) # Thoma

    msg_text += arr_text[random.randint(0,(len(arr_text)-1))]
    msg_text += '～～～～～♪♫♪♫'
    msg_text += chr(0)
    msg_text += '\n\n'

    for i in range(5):
        msg_text += '\n'

    payload2 = {
        "payload_json" : {
            'username': 'みんなのまま',
            'content' : '@here <@768119883283169300>',
            "avatar_url": "https://upload-os-bbs.hoyolab.com/upload/2022/11/24/21d71c44827fa664a6a21977d9a3dd1c_6799685155050732642.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png",
            "embeds": [],
        }
    }

    payload2['payload_json']['embeds'].append(
        {
            'color': 0x3556ca,
            'timestamp': datetime.datetime.now().isoformat(),
            'footer': {
                'text': 'Version: ' + '4.0'
                    + '#' + str( hex( zlib.crc32( str( math.floor( os.path.getmtime( __file__ ) ) ).encode() ) )[2:] ) + '',
            },
            "fields": [
                {
                    'inline': False,
                    'name'  : "",
                    'value' : msg_text
                            + '',
                }
            ],
        }
    )

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
                {
                    'color': 0x3556ca,
                    'url': 'https://twitter.com/Genshin_7',
                    "image": {
                        "url": 'attachment://' + file_name
                    },
                },
            )

    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': True,
            'name'  : "原神 (Genshin Impact)",
            'value' : ''
                    + ''
                    + '- [HoYoLAB: Daily Login Bounus](https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&lang=ja-jp)\n'
                    + '- [Ver.4.0公式PV](https://youtu.be/OlxaEK9K1Cs)\n'
                    + '- [Ver.4.0特設ページ](https://act.hoyoverse.com/ys/event/e20230805preview/index.html?game_biz=hk4e_global&hyl_presentation_style=fullscreen&hyl_landscape=true&hyl_hide_status_bar=true&utm_source=hoyolab&utm_medium=post)\n'
                    + '- [Ver.4.0新武器紹介](https://www.hoyolab.com/article/20789175)\n'
                    + '- [Ver.4.0新聖遺物紹介](https://www.hoyolab.com/article/20789174)\n'
                    + '',
        },
    )
    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': False,
            'name'  : '',
            'value' : chr(0),
        },
    )
    """ This Block is disabled
    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': False,
            'name'  : "原神 × Prime Gaming",
            'value' : ''
                    + ''
                    + '- [Prime Gaming: #8](https://gaming.amazon.com/genshin-impact-8)\n'
                    + '- [シリアルコード引換](https://genshin.hoyoverse.com/ja/gift)\n'
                    + '終了日: 2023年 5月25日 0:59 (JST)\n'
                    + '',
        },
    )
    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': False,
            'name'  : '',
            'value' : chr(0),
        },
    )
    """
    """ This Block is disabled
    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': False,
            'name'  : "原神予告番組最新情報",
            'value' : ''
                    + ''
                    + '- [HoYoLAB: Ver.3.7](https://genshin.hoyoverse.com/ja/news/detail/111406)\n'
                    + '- [Youtube](https://youtu.be/uda3T168Wpg)\n'
                    + '- [bilibili](http://live.bilibili.com/21987615)\n'
                    + '- [twitch](https://www.twitch.tv/genshinimpactofficial)\n'
                    + 'Time:  5月13日(土) 21:00 (JST)\n'
                    + '',
        },
    )
    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': False,
            'name'  : '',
            'value' : chr(0),
        },
    )
    """
    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': False,
            'name'  : "最新バージョン情報",
            'value' : ''
                    + ''
                    + '[Ver.4.0公式PV](https://youtu.be/OlxaEK9K1Cs)\n'
                    + '- [Ver.4.0特設ページ](https://act.hoyoverse.com/ys/event/e20230805preview/index.html?game_biz=hk4e_global&hyl_presentation_style=fullscreen&hyl_landscape=true&hyl_hide_status_bar=true&utm_source=hoyolab&utm_medium=post)\n'
                    + 'Time:  8月16日(水)  11:30 (JST)\n'
                    + 'Maintenance:  8月16日(水)  7:00 to 12:00 (JST)\n'
                    + '',
        },
    )
    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': False,
            'name'  : '',
            'value' : chr(0),
        },
    )
    """ This Block is disabled
    """
    payload2['payload_json']['embeds'][0]['fields'].append(
        {
            'inline': False,
            'name'  : '',
            'value' : chr(0),
        },
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

