import pyautogui as pgui
from time import sleep

if __name__ == '__main__':
    # 開始までの秒数を指定
    time = 3

    # 1回目のクリックする場所を指定
    x1 = 1910
    y1 = -103

    # 2回目のクリックする場所を指定
    x2 = 2846
    y2 = -94

    sleep(time)

    pgui.click(x=x1, y=y1)
    # pgui.doubleClick(x=x2, y=y2)
    pgui.click(x=x2, y=y2)
