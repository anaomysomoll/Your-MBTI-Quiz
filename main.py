import logging #Configures Python's built-in logging system to print timestamped messages
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
#specific classes from telegram bot library
from bot.handlers import start, button_handler
#functions start and button_handler from handlers.py
from config import BOT_TOKEN
#from config.py the hidden BOT_TOKEN

async def post_init(app): #Defining an asynchronous function (a function that lets other things run while waiting, non blocking)
    await app.bot.set_my_commands([ #Pauses here until the async task finishes, no blocking
        ("start", "Start the MBTI Quiz"),
    ]) #Tuples (command_name and description)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(post_init).build()
    # Method chaining, when each method returns the same object so we can keep calling
    # post_init is now hooked into the ONE app — slash menu will work correctly

    app.add_handler(CommandHandler("start", start))
    # A method that calling the /start command

    app.add_handler(CallbackQueryHandler(button_handler))
    # Register button click handler

    print("Bot is running...")
    app.run_polling(poll_interval=0.5) #infinite loop listening for telegram messages, 0.5s = faster response

if __name__ == "__main__":
    main() #This is in every Python file built-in variable
# __name__ == "__main__" only when run directly — prevents main() from running on import