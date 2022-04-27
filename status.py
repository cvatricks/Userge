import os
import time
import datetime

import pyrogram
from userge import userge, Config, logbot

#user_session_string = os.environ.get("user_session_string")
bots = [i.strip() for i in os.environ.get("BOTS").split(' ')]
bot_owner = Config.OWNER_ID
update_channel = os.environ.get("UPDATE_CHANNEL")
status_message_id = int(os.environ.get("STATUS_MESSAGE_ID"))
#api_id = int(os.environ.get("api_id"))
#api_hash = os.environ.get("api_hash")

#user_client = pyrogram.Client(
#    user_session_string, api_id=api_id, api_hash=api_hash)


def main():
    with userge:
            #while True:
            #print("[INFO] starting to check uptime..")
            logbot.reply_last_msg(f"[INFO] starting to check uptime..")
            edit_text = f"@{UPDATE_CHANNEL} Bot's Uptime Status.(Updated every day)\n\n"
            for bot in bots:
                #print(f"[INFO] checking @{bot}")
                logbot.reply_last_msg(f"[INFO] checking @{bot}")
                snt = userge.send_message(bot, '/start')

                time.sleep(15)

                msg = userge.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    #print(f"[WARNING] @{bot} is down")
                    logbot.reply_last_msg(f"[WARNING] @{bot} is down")
                    edit_text += f"@{bot} status: `Down`\n\n"
                    userge.send_message(bot_owner,
                                             f"@{bot} status: `Down`")
                else:
                    #print(f"[INFO] all good with @{bot}")
                    logbot.reply_last_msg(f"[INFO] all good with @{bot}")
                    edit_text += f"@{bot} status: `Up`\n\n"
                userge.read_history(bot)

            utc_now = datetime.datetime.utcnow()
            ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)

            edit_text += f"__last checked on \n{str(utc_now)} UTC\n{ist_now} IST__"

            userge.edit_message_text(UPDATE_CHANNEL, STATUS_MESSAGE_ID,
                                         edit_text)
            #print(f"[INFO] everything done! sleeping for 15 mins...")
            logbot.reply_last_msg(f"[INFO] everything done!")

            #time.sleep(15 * 60)