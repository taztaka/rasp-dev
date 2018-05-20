#!/usr/bin/python
# coding: utf-8
# 実行するコマンドを指定 (/usr/bin/python)
# エンコーディングを指定 (UTF-8)

# LED を消灯状態から完全に点灯状態になるまで徐々に明るくし、次に徐々に暗くする
# リスト型の変数 dc にデューティ比のリストを代入し、for ループで順番に
# デューティ比を取り出して、それに応じた PWM 信号を出力して LED を点灯させる
# このとき LED は徐々に明るくなる
# for ループを抜けた後、reverse メソッドを使ってリストの順番を逆にしているので、
# 再び for ループに入ると、今度は LED が徐々に暗くなる
# プログラムを終了するには、Python Shell を選択した状態で
# [Ctrl] + [c] キーを押下する

# GPIO ライブラリをインポート (RPi.GPIO を GPIO で別名表記)
import RPi.GPIO as GPIO
# time ライブラリをインポート
import time

# ピン番号の割り当て方式を「コネクタのピン番号」に設定
GPIO.setmode(GPIO.BOARD)

# 使用するピン番号を代入
LED = 40

# デューティ比のリストを作成
dc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 20, 30, 50, 70, 100]

# 11番ピンを出力ピンに設定し、初期出力をローレベルにする
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# PWM オブジェクトのインスタンスを作成
# 出力ピン：11番
# 周波数：100Hz
p = GPIO.PWM(LED, 100)

# PWM 信号を出力
p.start(0)

# 例外を検出する
try:
    # 無限ループ
    while 1:
        # デューティ比を 0～100 までリストに従って変化
        for val in dc:
            # デューティ比を設定
            p.ChangeDutyCycle(val)
            # 0.1秒待つ
            time.sleep(0.1)
        # リストの並び順を逆にする
        dc.reverse()
        # 0.1秒待つ
        time.sleep(0.1)

# キーボード例外を検出
except KeyboardInterrupt:
    # 何も処理しない
    pass

# PWM を停止
p.stop()

# GPIO を解放
GPIO.cleanup()
