# 押入れBOT

[![GitHub commit activity](https://img.shields.io/github/commit-activity/w/n138-kz/oshiire-bot)](/../../)
[![GitHub last commit](https://img.shields.io/github/last-commit/n138-kz/oshiire-bot)](/../../)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/n138-kz/oshiire-bot/Docker-test_dev.yml)](/../../actions)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/n138-kz/oshiire-bot/Docker-test_prd.yml)](/../../actions)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/n138-kz/oshiire-bot)](/../../)
[![GitHub repo file count](https://img.shields.io/github/directory-file-count/n138-kz/oshiire-bot)](/../../)
[![GitHub repo size](https://img.shields.io/github/repo-size/n138-kz/oshiire-bot)](/../../)
[![GitHub issues](https://img.shields.io/github/issues-raw/n138-kz/oshiire-bot)](/../../issues)
[![GitHub](https://img.shields.io/github/license/n138-kz/oshiire-bot)](/../../)
[![GitHub language count](https://img.shields.io/github/languages/count/n138-kz/oshiire-bot)](/../../)
[![GitHub top language](https://img.shields.io/github/languages/top/n138-kz/oshiire-bot)](/../../)

## How to run

1. Install the Docker [https://docs.docker.jp/docker-for-windows/install.html](https://docs.docker.jp/docker-for-windows/install.html)
1. Get Webhook URI [https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
![Images](https://support.discord.com/hc/article_attachments/1500000463501/Screen_Shot_2020-12-15_at_4.41.53_PM.png)
![Images](https://support.discord.com/hc/article_attachments/360101553853/Screen_Shot_2020-12-15_at_4.51.38_PM.png)
1. Create [`secret.yml`](#secretyml-gitignore) file to under `dev/` or `latest/`.
1. Run command the below ([#docker-build](#docker-build))
1. Run command the below ([#docker-run](#docker-run))

## Docker Build

```bash:docker-build
docker build -t n138-kz/oshiire-bot:dev dev/
docker build -t n138-kz/oshiire-bot latest/
```

## Docker Run

```bash:docker-run
docker run n138-kz/oshiire-bot:dev
```

## Items

- Dockerfile   -- Dockerfile
- images_001.png   -- 添付画像ファイル
- push.py   -- Script本体
- [secret.yml](#secretyml-gitignore)   -- Discord API エンドポイント
  
[![image](https://user-images.githubusercontent.com/8064928/226809337-e63f68b8-a846-4511-868f-f3c5f3e5bd5e.png)](/../../)

## secret.yml (gitignore)

```yaml:config.yml
credential:
  endpoint: https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxx?wait=true
```

[`?wait=true`][waitEqTrue] : [200OK][http200] の時 Responceを返すようになる。（デフォルトでは付いてない→ [204NoContent][http204]になる）

> waits for server confirmation of message send before response (defaults to `true`; when `false` a message that is not saved does not return an error)

[http200]: https://developer.mozilla.org/ja/docs/Web/HTTP/Status/200
[http204]: https://developer.mozilla.org/ja/docs/Web/HTTP/Status/204
[waitEqTrue]: https://discord.com/developers/docs/resources/webhook#execute-webhook

## Refs links

- [Discord Webhooks Guide | Structure of Webhook](https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html)
- [pythonからDiscordのwebhookでメッセージ投稿する備忘録 - Qiita](https://qiita.com/ABBBB/items/e6bdf7fc94b8f6f72a01)
- [（小ネタ）Discord WebhookでTwitterみたいな4枚画像を表示してみる - Qiita](https://qiita.com/GrapeColor/items/bdcf8431b13091447028)
- [Discord Developer Portal — Documentation — Webhook][waitEqTrue]
