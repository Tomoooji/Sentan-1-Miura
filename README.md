# Sentan-1-Miura

先端生命科学実験の三浦先生回分のプログラムフォルダ

## 環境構築メモ

python のバージョン: 3.10.9
→変更したい場合は.venvを消して作りなおす

ターミナルは+のところからコマンドプロンプトに切り替えてるけど、デフォルトのpowershellでも許可用のコマンド打てばvenvが動くらしい(ターミナルとかでC:\\Users\\...の前に(.venv)ってついてたらok)

ライブラリは通常通りpip istall して、そのあと

```
pip freeze > requirements.txt
```

を実行する



授業開始前のフォルダ構成

```
Sentan-1-Miura/
├─ .venv/
├─ README.md
└─ requirements.txt

```
