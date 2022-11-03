from telegram.ext import *
import api
from datetime import datetime

# import message_responses as r

import weather as wet

print("Bot started...")

def start_command(update, context):
    update.message.reply_text(
        """
        Hello! welcome to Weatherey.

Type /help to see the command details""")

def help_command(update, context):
    update.message.reply_text(
    """
    Command details:-

/help to see what can we do for you.
/team to see the details of developers.

You can write the city name to know the weather of that city.

Note:- Spell City name correctly to avoid errors.
    """
    )


now = datetime.now()
date_time = now.strftime(" Today is %d.%m.20%y and the time is %H:%M")
str(date_time)

def do_command(update, context):
    text = str(update.message.text).lower()
    response = wet.weather_response(text)
    
    update.message.reply_text(date_time)
    update.message.reply_text(response)
    update.message.reply_text("Thanks for using our Service :)")


def details_command(update, context):
    update.message.reply_text(
    """
    Our Team:-

    Rishabh Srivastava
    Priyambada Modanval
    Ayush Tripathi @the_ayushtripathi
    """
    )

def stop_command(update, context):
    update.message.reply_text("Thanks for using our services, Regards our team.")


def main():
    updater= Updater(api.telegram_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("team", details_command))
    dp.add_handler(CommandHandler("stop", stop_command))
    # dp.add_handler(CommandHandler("weather", weather_command))
    # dp.add_handler(MessageHandler(Filters.text, weather_command))
    dp.add_handler(MessageHandler(Filters.text, do_command))

    updater.start_polling(3)
    updater.idle()

main()