from pywinauto import application
import time
app = application.Application()
app.start("Notepad.exe")

app.Notepad.wait('ready')
app.Notepad.edit.type_keys("Hellou hear")
app.Notepad.menu_select("File->SaveAs")
#time.sleep(1)
app.Notepad.Save_as.edit.SetText("Hellou hear.txt")
