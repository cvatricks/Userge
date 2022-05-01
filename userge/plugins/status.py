import os
import time
import datetime

import pyrogram
from userge import userge, Config
CHANNEL = userge.getCLogger(__name__)

async def main():
            #user_session_string = os.environ.get("user_session_string")
            bots = [i.strip() for i in os.environ.get("BOTS").split(' ')]
            bot_owner = os.environ.get("OWNER_ID")
            update_channel = os.environ.get("UPDATE_CHANNEL")
            status_message_id = int(os.environ.get("STATUS_MESSAGE_ID"))
            #api_id = int(os.environ.get("api_id"))
            #api_hash = os.environ.get("api_hash")
            #user_client = pyrogram.Client(
            #    user_session_string, api_id=api_id, api_hash=api_hash)
            #while True:
            #print("[INFO] starting to check uptime..")
            ###await CHANNEL.log(f"[INFO] starting to check uptime..")
            edit_text = f"🤖 **Bot's uptime status** (Updated every day)\n\n"
            for bot in bots:
                #print(f"[INFO] checking @{bot}")
                ###await CHANNEL.log(f"[INFO] checking @{bot}")
                snt = await userge.send_message(bot, '/start')

                time.sleep(15)

                msg = (await userge.get_history(bot, 1))[0]
                if snt.message_id == msg.message_id:
                    #print(f"[WARNING] @{bot} is down")
                    ###await CHANNEL.log(f"[WARNING] @{bot} is down")
                    edit_text += f"🔴 @{bot} : **Offline**\n\n"
                    await userge.send_message(bot_owner,
                                             f"🔴 @{bot} : **Offline**")
                else:
                    #print(f"[INFO] all good with @{bot}")
                    ###await CHANNEL.log(f"[INFO] all good with @{bot}")
                    edit_text += f"🟢 @{bot} : **Online**\n\n"
                await userge.read_history(bot)

            utc_now = datetime.datetime.utcnow()
            ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)

            edit_text += f"**⌚ last checked on** \nUTC => {str(utc_now)}\nIST => {ist_now}**"

            await userge.edit_message_text(update_channel, status_message_id,
                                         edit_text)
            #print(f"[INFO] everything done! sleeping for 15 mins...")
            ###await CHANNEL.log(f"[INFO] everything done!")

            #time.sleep(15 * 60)
            
#@userge.on_start
async def _init():
      await main()
