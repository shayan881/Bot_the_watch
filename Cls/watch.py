from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import jdatetime

from random import randint

class Watch:
    def RandInt()-> int:
        x = randint(0, 255)
        y = randint(0, 255)
        z = randint(0, 255)
        return x,y,z
        
    def Time()-> str:
        NewTime = jdatetime.datetime.now().strftime("shayan->\n%a, %d %b \n %Y %H:%M")
        return NewTime

    def GetPhoto():
        img = Image.open(r'Cls/watch.jpg')
        I1 = ImageDraw.Draw(img)
        MyFont = ImageFont.truetype('FreeMono.ttf', 12)
        I1.text((120,140), Watch.Time(),font=MyFont, fill=(Watch.RandInt()))

        img.save('Cls/wathsave.jpg')


