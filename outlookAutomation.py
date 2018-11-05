import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
messages = inbox.Items
message = messages.GetLast()
body_content = message.body
print(body_content)
print("")
for i in range(50):
    try:
        box = outlook.GetDefaultFolder(i)
        name = box.Name
        print(i, name)
    except:
        pass