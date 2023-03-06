# 押入れBOT

![GitHub commit activity](https://img.shields.io/github/commit-activity/w/n138-kz/oshiire-bot)
![GitHub last commit](https://img.shields.io/github/last-commit/n138-kz/oshiire-bot)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/n138-kz/oshiire-bot/dev.yml)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/n138-kz/oshiire-bot)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/n138-kz/oshiire-bot)
![GitHub repo size](https://img.shields.io/github/repo-size/n138-kz/oshiire-bot)
![GitHub issues](https://img.shields.io/github/issues-raw/n138-kz/oshiire-bot)
![GitHub](https://img.shields.io/github/license/n138-kz/oshiire-bot)
![GitHub language count](https://img.shields.io/github/languages/count/n138-kz/oshiire-bot)
![GitHub top language](https://img.shields.io/github/languages/top/n138-kz/oshiire-bot)

```bash:docker-build
docker build -t n138-kz/oshiire-bot:dev dev/
docker build -t n138-kz/oshiire-bot latest/
```

```bash:docker-run
docker run n138-kz/oshiire-bot:dev
```

## Items

- Dockerfile   -- Dockerfile
- images_001.png   -- 添付画像ファイル
- push.py   -- Script本体
- secret.yml   -- Discord API エンドポイント

## config.yml (gitignore)

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
- [pythonからDiscordのwebhookでメッセージ投稿する備忘録](https://qiita.com/ABBBB/items/e6bdf7fc94b8f6f72a01)
