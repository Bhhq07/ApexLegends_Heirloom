#!/usr/bin/python3

import time
import pyautogui


pyautogui.PAUSE=1
l,t,w,h=pyautogui.locateOnScreen('setting.png')
setting=pyautogui.center((l,t,w,h))

l,t,w,h=pyautogui.locateOnScreen('legend.png')
legend=pyautogui.center((l,t,w,h))

pyautogui.click(setting)

l,t,w,h=pyautogui.locateOnScreen('r.png')
r=pyautogui.center((l,t,w,h))

pyautogui.click(r)

l,t,w,h=pyautogui.locateOnScreen("yes.png")
yes=pyautogui.center((l,t,w,h))

pyautogui.click(yes)

l,t,w,h=pyautogui.locateOnScreen("goon.png")
goon=pyautogui.center((l,t,w,h))

pyautogui.click(goon)

time.sleep(5)

pyautogui.click(legend)

l,t,w,h=pyautogui.locateOnScreen("wraith.png")
wraith=pyautogui.center((l,t,w,h))

while True:
    pyautogui.press('esc')
    pyautogui.press('esc')
    pyautogui.click(setting)
    pyautogui.click(r)
    pyautogui.click(yes)
    pyautogui.click(goon)
    time.sleep(4)
    pyautogui.click(legend)
    pyautogui.click(wraith)
    
    l,t,w,h=pyautogui.locateOnScreen('heirloom.png')
    if l!=None:
        break
i=0
while i<5:
    print('成功！')
    i=i+1


    
    
