# import qrcode
# from pyzbar.pyzbar import decode

# def QrCreator():
#     qr = qrcode.QRCode(
#     version=10,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
#     )
#     qr.add_data("sdksjfssssccccccccccccccccccccccccccccccccscscsksfjsfjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjsssssfdddddddddddddddddddddddddddddddddddddddddddddda")
#     qr.make(fit=True)


#     img = qr.make_image(fill_color="green", back_color="black")
#     img.save('QrCode.jpg')




# def decodeQr(update: Update, context: CallbackContext):
#     	chat_id = update.message.chat_id

# 	if update.message.photo:
# 		id_img = update.message.photo[-1].file_id
# 	else:
# 		return

# 	foto = context.bot.getFile(id_img)

# 	new_file = context.bot.get_file(foto.file_id)
# 	new_file.download('qrcode.png')

# 	try:
# 		result = decode(Image.open('qrcode.png'))
# 		context.bot.sendMessage(chat_id=chat_id, text=result[0].data.decode("utf-8"))
# 		os.remove("qrcode.png")
# 	except Exception as e:
# 		context.bot.sendMessage(chat_id=chat_id, text=str(e))