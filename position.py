import pyautogui as pgui
from time import sleep

if __name__ == '__main__':
    # 開始までの秒数を指定
    time = 3

    sleep(time)
    posisiton = pgui.position()
    print(posisiton)
