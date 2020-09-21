"""Userbot start point"""

from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


LOGS.info("You are running CaptainAmericaUserBot[ver : MORE & MORE]")

LOGS.info(
    "Congratulations, your userbot is now running !!"
    "Test it by typing .alive, .on or .alive in any chat."
    "for further assistance, head to https://t.me/captainAmericaUserbotSupport")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
