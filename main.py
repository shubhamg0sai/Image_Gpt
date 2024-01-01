import datetime
import os
from PIL import Image
from datetime import datetime
from wish.wish import speak , wish
from voiceinp.voiceinp import voiceinp
from ai.ai import  imgai

x=datetime.now()
t = x.strftime('%I:%M:%p')
y = x.year
d = x.strftime('%A')
wish()
if __name__ == '__main__':
    while True:
        print (t, y)
        print(d)
        query = voiceinp().lower()
        imgai(query)
        img = Image.open("image.png")
        img.show()
        os.remove("image.png")
