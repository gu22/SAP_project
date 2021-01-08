# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:35:15 2020

@author: GLPYZ

Automate Win\SAP

"""


import easygui
from easygui import *
import time
import subprocess
import login
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pathlib
from pathlib import Path
import easygui
import keyboard
from win10toast import ToastNotifier

valores = easygui.enterbox("Remessas")

valores = valores.split(',')

toaster = ToastNotifier()

path = ('C:\\Users\\Public\\GLPYZ\\WPy64-3771\\python-3.7.7.amd64\\Winium.Desktop.Driver.exe')

winium = subprocess.Popen(path)

# driver = webdriver.Remote(
#     command_executor='http://localhost:9999',
#     desired_capabilities={
#         'app': r'C:\Program Files (x86)\SAP\FrontEnd\SapGui\saplogon.exe'
#     })

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        'app': r'C:\Users\TEMP.AD-BAYER-CNB.001\Desktop\P08 SAP Easy Access.sap'
    })

word = "teste"

action = ActionChains(driver)



time.sleep(6)
print("ACESSANDO\n>>>>>")
elemento = driver.find_element_by_id("1005")
elemento.click()
elemento.send_keys(word)
# b = driver.find_element_by_id("1")
b = driver.find_element_by_name("Logon")
b.click()





time.sleep(10)
msg = ("Iniciando processo...\n")
print(msg)
toaster.show_toast("",msg,duration=3)
c = driver.find_element_by_id("1001")
# c.click()
c.send_keys("vl02n")
# c.send_keys(Keys.ENTER)
c.submit()

time.sleep(1)
# easygui.msgbox('Aguardar')

for i in valores:
    time.sleep(5)
    pane = driver.find_element_by_id('100')
    pane.send_keys(i)
    # pane.send_keys(Keys.RETURN)
    pane.submit()
    
    
    # action.key_down(Keys.SHIFT)
    # action.send_keys(Keys.F2)
    # action
    time.sleep(2)
    msg=(f"====[ELIMINANDO - {i}]=======")
    print(msg)
    toaster.show_toast("",msg,duration=3)
    # x = driver.find_element_by_class_name('Eliminar')
    x = driver.find_element_by_id('125')
    x.click()
    # action.send_keys(Keys.SHIFT,Keys.TAB,Keys.SHIFT).perform()
    time.sleep(1)
    
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('enter')
    
    time.sleep(1)
    
    with open("log_x.txt",'a') as wr:
        wr.write(f'{i}\n')
        
    # easygui.msgbox("Continuar")
    # time.sleep(3)
    # dialog =driver.find_element_by_id('101')
    
    # # action.send_keys(Keys.TAB).build().perform()
    
    # dialog.send_keys('{TAB}')
# dialog.send_keys(Keys.TAB)
# dialog.send_keys(Keys.RETURN)

driver.close()
winium.terminate()



# actionchains = ActionChains(driver)
# actionchains.send_keys("teste")
# (elemento).perform()

# usuario = login.usuario()
# senha = login.senha()