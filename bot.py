import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
import qrcode
from pyzbar.pyzbar import decode
from telegram import Update
from PIL import Image

PORT = int(os.environ.get('PORT'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = os.environ.get('TOKEN')


def QrCreator(update, context):
    qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    info = update.message.text
    qr.add_data(str(info))
    qr.make(fit=True)


    img = qr.make_image(fill_color="green", back_color="black")
    img.save('QrCode.png')

    ft = open('QrCode.png','rb')
    update.message.reply_photo(photo=ft, caption=info)
    os.remove("QrCode.png")
   

def decodeQr(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if update.message.photo:
    	    id_img = update.message.photo[-1].file_id
    else:
       return

    foto = context.bot.getFile(id_img)
    new_file = context.bot.get_file(foto.file_id)
    new_file.download('qrcode.png')
    try:
        result = decode(Image.open('qrcode.png'))
        context.bot.sendMessage(chat_id=chat_id, text=result[0].data.decode("utf-8"))
        os.remove("qrcode.png")
    except Exception as e:
        context.bot.sendMessage(chat_id=chat_id, text=str(e))
	

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text( 
        """Hola con este bot puedes crear y leer codigos Qr.
        Para crear un Qr solo manda un mensaje con el contenido del qr.
        Para leer el Qr manda una foto del mismo.
    """)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, QrCreator))
    dp.add_handler(MessageHandler(Filters.photo, decodeQr))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://qr-creator-bot.herokuapp.com/' + TOKEN)


    updater.idle()
    # updater.start_polling()

if __name__ == '__main__':
    main()


