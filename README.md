# Pacman Project

プロジェクトの概要をここに記載します．
このREADMEは雛形ですので，適宜修正してください．

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

- 指定できるパラメータは以下の通り．
```json
{
    "param1": 0,    # ダミーのパラメータ1
    "param2": {     # ダミーのパラメータ2
        "k1": "v1",
        "k2": "v2"
    }
}
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── config.py #パラメータの定義
├── controller.py # キーボードからの入力を受け取るクラス
├── field.py # Fieldクラスはゲームのフィールドを担うクラス。フィールドの初期化やディスプレイを行なう。
├── game.py # ゲームの初期設定とメインループを実行してゲームを実施するクラス
├── item.py # Playerの親クラス
├── main.py #　実行ファイル
├── player.py #　playerクラス
├── requirements.txt #　バージョン記載
├── parameters.json #パラメータ指定用ファイル
├── result # 結果出力ディレクトリ
│   └── 20241112_174710
│       ├── log.log
│       └── parameters.json
└── utils.py # 共有関数群
```
\