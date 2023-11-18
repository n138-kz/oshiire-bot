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

## 基本設計 / Basic Design Documents

- Discord server に対し指定したメッセージをPOSTするプログラムである。
- プログラム開発言語は `python3` とする。(`python2`との互換性は無い)
- ソースコードは 改版履歴管理プログラムプロパイダーである `GitHub` を使用する。
- オープンソース状態とし、利用者にもソースコード閲覧可とするため、Repositoryの公開設定は `PUBLIC` とする。
- 開発用PCのローカル側では `git` を使用する。
- Discord server へのアクセスキー（トークン）については、ソースコードを `Github` へアップロードすることより、ソースコードとは別ファイルにするものとし、`GitHub` へのアップロードは行わない。
- 誤ってDiscord server へのアクセスキーを漏洩（アップロード）してしまった場合は直ちに当該アクセスキーの無効化を行う。
- 環境は `docker` によってコンテナ化し、`docker`実行環境を整えれば実行可能にできるものとする。

## Refs links

- [Discord Webhooks Guide | Structure of Webhook](https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html)
- [pythonからDiscordのwebhookでメッセージ投稿する備忘録 - Qiita](https://qiita.com/ABBBB/items/e6bdf7fc94b8f6f72a01)
- [（小ネタ）Discord WebhookでTwitterみたいな4枚画像を表示してみる - Qiita](https://qiita.com/GrapeColor/items/bdcf8431b13091447028)
- [Discord Developer Portal — Documentation — Webhook][waitEqTrue]
