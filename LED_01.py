#!/usr/bin/python
# coding: utf-8
# 実行するコマンドを指定 (/usr/bin/python)
# エンコーディングを指定 (UTF-8)

# LED を接続した11番の GPIO ピンの出力信号を、無限ループの中で
# ハイレベルとローレベルに交互に切り替えている
# このプログラムを実行すると、0.5秒間隔で LED が点滅する
# プログラムを終了するには、Python Shell を選択した状態で
# [Ctrl] + [c] キーを押下する

# GPIO ライブラリをインポート (RPi.GPIO を GPIO で別名表記)
import RPi.GPIO as GPIO
# time ライブラリをインポート
import time

# 拡張コネクタのピン番号の割り当て方式を「ピン番号」に設定
# GPIO.BCM の場合は「ピン名」に設定される
GPIO.setmode(GPIO.BOARD)

# 使用するピン番号を代入
LED = 40

# 11番ピンを出力ピンに設定し、初期出力をローレベルにする
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# 例外を検出する
try:
    # 無限ループ (プログラムを停止するための処理が必要)
    while 1:
        # ハイレベルを出力
        GPIO.output(LED, GPIO.HIGH)

        # 0.5秒待つ
        time.sleep(0.5)

        # ローレベルを出力
        GPIO.output(LED, GPIO.LOW)

        # 0.5秒待つ
        time.sleep(0.5)

# キーボード例外を検出
except KeyboardInterrupt:
    # 何も処理しない
    pass

# GPIO を解放
GPIO.cleanup()
