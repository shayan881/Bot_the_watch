# ▂▃▅▇█▓▒░   Telegram : @ShayanHeydari3 ░▒▓█▇▅▃▂

from pyrogram import Client, filters
from pyrogram.types import Message
from Cls.set_time_information import SetTimeInformation

app = Client(
    name="TheWatch",
    api_id=None,
    api_hash=None,
)

Wath = SetTimeInformation(client=app)

@app.on_message(filters.me & filters.text)
def On_Msg(client, message:Message):
    Text = message.text

    if Text == 'On':
        if not Wath.status:
            message.reply_text(
                'ساعت روشن شد ...'
            )
            Wath.Start()
        else:
            message.reply_text(
                    'ساعت روشن است'
                )

    elif Text == 'Off':
        if Wath.status:
            Wath.Stop()
            message.reply_text(
                'ساعت خاموش شد'
            )

        else:
            message.reply_text(
                'ساعت خاموش است'
            )

if __name__ == '__main__':
    app.run()

# ▂▃▅▇█▓▒░   Telegram : @ShayanHeydari3 ░▒▓█▇▅▃▂
