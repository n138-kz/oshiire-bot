# 押入れBOT

```bash
docker build -t n138-kz/oshiire-bot:dev /mnt/edisk01/oshiire-bot/dev/ && docker build -t n138-kz/oshiire-bot /mnt/edisk01/oshiire-bot/latest/
```

## config.yml (gitignore)

```yaml:config.yml
credential:
  endpoint: https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxx?wait=true
```

[`?wait=true`][waitEqTrue] : [200OK][http200] の時 Responceを返すようになる。（デフォルトでは付いてない→ [204NoContent][http204]になる）

[http200]: https://developer.mozilla.org/ja/docs/Web/HTTP/Status/200
[http204]: https://developer.mozilla.org/ja/docs/Web/HTTP/Status/204
[waitEqTrue]: https://discord.com/developers/docs/resources/webhook#execute-webhook

## Refs links
- https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
- https://qiita.com/ABBBB/items/e6bdf7fc94b8f6f72a01
