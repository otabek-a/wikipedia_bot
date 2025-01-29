from telegram.ext import CallbackContext,Filters,MessageHandler,Updater,CommandHandler
import wikipedia
from telegram import ReplyKeyboardMarkup
import os
def start(update,context):
    reply_key=[
        ['/start'],
    ]
    make=ReplyKeyboardMarkup(reply_key)
    update.message.reply_text('salom, iltimos malumot qidirsih uchun mendan biron nima surang',reply_markup=make)

def wiki(update,context):
    try:
        wikipedia. set_lang ("uz" )
        page=wikipedia.page(update.message.text)
        update.message.reply_photo(page.images[0],caption=f'{wikipedia.summary(update.message.text)}')
        
    except:
        update.message.reply_text('I am sorry i couldnot find any informatin')
        update.message.reply_text('kechirasiz bunaqangi malumot topolmadim')
updater=Updater(token=os.environ['TOKEN'])
dispatcher=updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))

dispatcher.add_handler(MessageHandler(None,wiki))
updater.start_polling()
updater.idle()


