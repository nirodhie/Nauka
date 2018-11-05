from pywinauto import application
from pywinauto import findwindows
from pywinauto.controls.win32_controls import ButtonWrapper
import time
import os

os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"}) #pomija UAC !!!
app = application.Application()
app.start(r"C:\Program Files (x86)\Microsoft Office\root\Office16\OUTLOOK.EXE")
app.Outlook.menu_select("File")



'''
app.Notepad.edit.type_keys("Hellou hear")
app.Notepad.menu_select("File->SaveAs")
#time.sleep(1)
app.Notepad.Save_as.edit.SetText("Hellou hear.txt")
'''