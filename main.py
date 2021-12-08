import logging
from telegram.ext import *
from telegram import *
from others import *
from url_img_callback import *
from callback import *
from Other_imgs import *
from config import Config




# Set up the logging





    






API_KEY = '2076230938:AAHzms8SVRsfMoWEC10nf18ECcbWWiY6UpI'



updater = Updater(token=Config.TG_BOT_TOKEN)
dispatcher = updater.dispatcher






def start_command(update, context):
    context.bot.send_sticker(chat_id=update.message.chat_id,sticker='CAACAgIAAxkBAAEDPtphimNfKxHhaiYHken1jE7VK1IQ3gACmhAAAsaV0Uub173UMeyuHCIE')
    context.bot.send_message(chat_id=update.message.chat_id, text='''
You can get a lot of pictures of Emma Watson from this bot 
    ''' , reply_markup=ReplyKeyboardMarkup(firstbuttonset))
    
    

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')

















dispatcher.add_error_handler(error)
dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(CallbackQueryHandler( queryHandler))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))







    # Run the bot
updater.start_polling()





