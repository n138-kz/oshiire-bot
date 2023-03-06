# 押入れBOT

```bash
docker build -t n138-kz/oshiire-bot:dev /mnt/edisk01/oshiire-bot/dev/ && docker build -t n138-kz/oshiire-bot /mnt/edisk01/oshiire-bot/latest/
```

## config.yml (gitignore)

```yaml:config.yml
credential:
  endpoint: https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxx?wait=true
```

`?wait=true` : 200OK の時 Responceを返すようになる。（デフォルトでは付いてない→ 204Nothingになる）
