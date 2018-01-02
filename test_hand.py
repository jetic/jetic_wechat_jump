import time
import win32api, win32gui, win32con
from ctypes import *
import math

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
    
def colorEqual(c1, c2):
    if (abs(c1[0]-c2[0])+abs(c1[1]-c2[1])+abs(c1[2]-c2[2]) < 2):
        return True
    else:
        return False
    
def colorLike(c1, c2):
    if (abs(c1[0]-c2[0])+abs(c1[1]-c2[1])+abs(c1[2]-c2[2]) < 30):
        return True
    else:
        return False   
        
def colorLike2(c1, c2):
    if (abs(c1[0]-c2[0])+abs(c1[1]-c2[1])+abs(c1[2]-c2[2]) < 45):
        return True
    else:
        return False
    
def findPixel(c, x1, y1, x2, y2):
    for j in range(y2+1, y1, -1):
        for i in range(x1, x2+1):
            c2 = getPixel(i, j)
            if colorEqual(c, c2):
                return i, j

def main():
    screen_mid_x = 382
    screen_left_x = 125
    screen_right_x = 643
    background_point = (300, 260)
    dummy_color = (60, 69, 104)
    white_color = (235, 235, 235)
    go_k = 0.625
    time_scale_x = 300.0
    center_to_edge = 50
    go_right = True
    
    for i in range(300):
        dummy_pos = findPixel(dummy_color, 168, 525, 622, 630)
        """
#        if (not dummy_pos):
#            continue
        moveCurPos(dummy_pos[0], dummy_pos[1])
        if (dummy_pos[0] < screen_mid_x):
            go_right = True
        else:
            go_right = False
        new_background_color = getPixel(background_point[0], background_point[1])
        last_background_color = (0, 0, 0)
        while (not colorEqual(last_background_color, new_background_color)):
            time.sleep(0.1)
            last_background_color = new_background_color
            new_background_color = getPixel(background_point[0], background_point[1])
        background_color = new_background_color
        print background_color
        dx = 0
        onTarget = False
        if (go_right):
            for target_x in range(screen_right_x, dummy_pos[0], -1):
                target_y = int(dummy_pos[1] - (target_x - dummy_pos[0]) * go_k)
                target_color = getPixel(target_x, target_y)
#                print target_x, target_y, target_color
                if (not onTarget):
                    if (not colorLike(target_color, background_color)):
                        dx = target_x - dummy_pos[0]
                        print target_x, target_y, target_color, dx
                        onTarget = True
                        saved_target_color = target_color
                        saved_target_x = target_x
                elif ((not colorLike(target_color, saved_target_color)) and (not colorLike2(target_color, white_color))):
                    if (saved_target_x - target_x > 35):
                        dx -= (saved_target_x - target_x) / 2
                    else:
                        dx -= center_to_edge
                    break
        else:
            for target_x in range(screen_left_x, dummy_pos[0], 1):
                target_y = int(dummy_pos[1] - (dummy_pos[0] - target_x) * go_k)
                target_color = getPixel(target_x, target_y)
#                print target_x, target_y, target_color
                if (not onTarget):
                    if (not colorLike(target_color, background_color)):
                        dx = dummy_pos[0] - target_x
                        print target_x, target_y, target_color, dx
                        onTarget = True
                        saved_target_color = target_color
                        saved_target_x = target_x
                elif ((not colorLike(target_color, saved_target_color)) and (not colorLike2(target_color, white_color))):
                    if (target_x - saved_target_x > 35):
                        dx -= (target_x - saved_target_x) / 2
                    else:
                        dx -= center_to_edge
                    break
        
        if (go_right):
            target_center_x = dummy_pos[0] + dx
        else:
            target_center_x = dummy_pos[0] - dx
        target_center_y = int(dummy_pos[1] - dx * go_k)
        moveCurPos(target_center_x, target_center_y)
        print i, dx/time_scale_x
        
        """
        
        moveCurPos(1547, 959)
        clickLeftCur()
        moveCurPos(404, 509)
        X = raw_input()
        if (X == "1"):
            break
        point = getCurPos()
        dx = abs(point[0] - dummy_pos[0])
        dy = abs(point[1] - dummy_pos[1])
        distance = math.sqrt(dx * dx + dy * dy)
        holdLeftCur(distance / 360.0)
        

main()