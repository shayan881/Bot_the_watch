from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import jdatetime

from random import randint

class Watch:
    
    def RandInt()-> int:

        """ Create number random for color random """

        x = randint(0, 255)
        y = randint(0, 255)
        z = randint(0, 255)
        return x,y,z
        
    def Time()-> str:

        """ return time """

        NewTime = jdatetime.datetime.now().strftime("shayan->\n%a, %d %b \n %Y %H:%M")
        return NewTime

    def GetPhoto():

        """ Create Image and Save with name wathsave.jpg"""

        img = Image.open(r'Cls/watch.jpg')
        I1 = ImageDraw.Draw(img)
        MyFont = ImageFont.truetype('Cls/BebasNeue-Regular.ttf', 15)
        I1.text((120,140), Watch.Time(),font=MyFont, fill=(Watch.RandInt()))

        img.save('Cls/wathsave.jpg')


