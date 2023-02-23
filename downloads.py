from requests import get
import shutil # save img locally

url = 'https://drive.google.com/u/0/uc?id=1DcjtEpoI5kAHTld610Bdk6sUwrC4p34G&export=download'
res = get(url, stream = True)

if res.status_code == 200:
    with open('file.jpg','wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ','file.jpg')
else:
    print('Image Couldn\'t be retrieved')