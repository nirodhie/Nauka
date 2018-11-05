import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

#inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder

inbox = outlook.Folders['Lukasz.Teska@bd.com'].Folders['Skrzynka odbiorcza'].Folders['New users']
messages = inbox.Items
message = messages.GetLast()

subject = "Onboarding (Wroclaw) - 19.11.2018"
while message:
    if subject in message.Subject and "RE:" not in message.Subject and "FW:" not in message.Subject:
        print(message.subject.lstrip(subject)) # usun czesc tytulu ktora poszukujemy bo jest dla wszystkich taka sama
        print(message.body.splitlines()[20])
        print(message.body.splitlines()[24])
        print(message.body.splitlines()[28])
        print(message.body.splitlines()[32])
        
        print()
    message = messages.GetPrevious()

'''
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
subject = "Onboarding (Wroclaw) - 19.11.2018"
message = messages.getfirst()
while message:
    message.subject
    message = messages.GetNext()

'''
'''
for i in range(50):
    try:
        box = outlook.GetDefaultFolder(i)
        name = box.Name
        print(i, name)
    except:
        pass
'''