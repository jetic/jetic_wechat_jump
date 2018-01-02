import time
import win32api, win32gui, win32con
from ctypes import *

def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def holdLeftCur(t):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)    
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def moveCurPos(x, y):
    windll.user32.SetCursorPos(x, y)

def getCurPos():
    return win32gui.GetCursorPos()

def getPixel(x, y):
    hwnd = win32gui.WindowFromPoint((x, y))  
    hdc = win32gui.GetDC(hwnd)  
    x1, y1 = win32gui.ScreenToClient(hwnd, (x, y))  
    color = win32gui.GetPixel(hdc, x1, y1)  
    win32gui.ReleaseDC(hwnd, hdc)
    return color%256, color/256%256, color/256/256

def main():
    print getPixel(getCurPos()[0], getCurPos()[1])
    point = getCurPos()
    print point

main()