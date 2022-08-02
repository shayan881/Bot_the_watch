import time 
import jdatetime

from pyrogram import Client
from Cls.watch import Watch


class SetTimeInformation:
    status = False
    def __init__(
            self,
            client:Client
    ) -> None:
        
        self.client = client
        
    def Start(self):

        """ Starting the watch """

        self.status = True
        self.TimeCheck()

    def Stop(self):

        """ Stoping the watch """

        self.status = False

    def TimeCheck(self):

        """ setting watch """

        #< ------------ >
            # For Set One Profile
        NewTime = jdatetime.datetime.now().strftime("%M")
        Watch.GetPhoto()
        self.client.set_profile_photo(photo='Cls/wathsave.jpg')
        #< ------------ >

        while self.status:
            Time = jdatetime.datetime.now().strftime("%M")
            if Time != NewTime:
                NewTime = Time
                Watch.GetPhoto()
                photos = list(self.client.get_chat_photos('me'))
                self.client.delete_profile_photos(photos[0].file_id)
                self.client.set_profile_photo(photo='Cls/wathsave.jpg')
            print(NewTime)
            time.sleep(2)
        else:
            # Delete profile watch
            photos = list(self.client.get_chat_photos('me'))
            self.client.delete_profile_photos(photos[0].file_id)



