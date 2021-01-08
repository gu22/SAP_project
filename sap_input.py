# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:52:09 2021

@author: GLPYZ
"""

import easygui
import time
import keyboard as kb
from win10toast import ToastNotifier


toaster = ToastNotifier()

valores = easygui.enterbox()
valores = valores.split(',')


# if valores is not list:
#     x = valores
#     valores = []
#     valores.append(x)

easygui.msgbox("COMEÇAR?")
time.sleep(5)

for i in valores:
    kb.write(i)
    kb.send('enter')
    time.sleep(5)
    kb.send('f8')
    time.sleep(1)
    kb.send('tab')
    for i in range(10):
        kb.send('right')
    kb.send('enter')
    
    # easygui.msgbox("Continuar?")
    if easygui.ynbox() == True:
        kb.send('ctrl+s')
        time.sleep(3)
    else:
        toaster.show_toast("","Finalizado - break",duration=2)
        break
    
toaster.show_toast("","Finalizado",duration=2)      
    
    

