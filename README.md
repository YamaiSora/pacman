# Pacman Project

本プログラムは、パックマンをターミナル上で動かすプログラムです。
パックマンを3×3のフィールドで動かすことができる。

## Requirement
- Python 3.12.5
- flake8 7.1.1
- mccabe 0.7.0
- pycodestyle 2.12.1
- pyflakes 3.2.0

## Installation
- 結果出力用ディレクトリを作成
```shell
mkdir result
```
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```


## Usage
- メインプログラムを実行．
  - `result/[日付][実行時刻]/` 下に実行結果とログが出力されます．
```shell
python main.py
```
- デフォルトのパラメータ設定をjson出力．
```shell
python config.py  # parameters.jsonというファイルが出力される．
```
- 以下のように，上記で生成されるjsonファイルの数値を書き換えて，実行時のパラメータを指定できます．
```shell
python main.py -p parameters.json
```
- 詳しいコマンドの使い方は以下のように確認できます．
```shell
python main.py -h
```


## Parameter Settings

- 指定できるパラメータはなし.

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── README.md
├── config.py
├── controller.py
├── field.py
├── game.py
├── item.py
├── main.py
├── player.py
├── requirements.txt
├── result
│   ├── 20240910_162750
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241105_172507
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_165507
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_165932
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_170131
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_170155
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_170414
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_170632
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_172340
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_172411
│   │   ├── log.log
│   │   └── parameters.json
│   ├── 20241112_174603
│   │   ├── log.log
│   │   └── parameters.json
│   └── 20241112_174710
│       ├── log.log
│       └── parameters.json
└── utils.py
```
\