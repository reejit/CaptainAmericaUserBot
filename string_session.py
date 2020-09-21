from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""THIS is the string session Generator of Captain America UserBot
PLEASE FOLLOW INSTRUCTIONS FOR BETTER CHANCES OF SUCCESS....""")
API_KEY = int(input("Enter API_KEY here: "))
API_HASH = input("Enter API_HASH here: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Check your Telegram Saved Messages to copy the STRING_SESSION value")
    session_string = client.session.save()
    saved_messages_template = """Support: @CaptainAmericaUserBotSupport
<code>STRING_SESSION</code>: <code>{}</code>
⚠️ <i>Check Your Saved Messages for your String Session</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
