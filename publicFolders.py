# publicFolders.py
# still a work in progress

import requests
import shutil

folderId = "1oqi5JJW0UEsMCeqrt2qnNUcQ0pHakuMm"
apiKey = [YOUR_API_KEY]

folder = f"https://www.googleapis.com/drive/v3/files?q=%27{folderId}%27%20in%20parents&key={apiKey}"

results = requests.get(folder)
list = results.json()['files']
for item in list:
    name = item['name']
    id = item['id']

    url = f'https://drive.google.com/u/0/uc?id={id}&export=download'
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',name)
    else:
        print('Image Couldn\'t be retrieved')

