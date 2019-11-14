from config import bot_token, storage_path
from image_processing import process_image
import telebot
import logging
import time
import os

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

bot = telebot.TeleBot(bot_token)
upd = bot.get_updates()

try:
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        try:
            welcome_text = 'Hi! I am UMA Bot and I was created to classify pictures for you :) Please, upload a picture to classify.'
            bot.send_message(chat_id=message.chat.id, text=welcome_text, reply_to_message_id=message.message_id)
        except Exception as e:
            logger.error("ExceptionFromStart: " + str(e))
            pass

    @bot.message_handler(content_types=['photo'])
    def handle_photo_msg(message):
        try:
            if not os.path.exists(storage_path):
                os.makedirs(storage_path, exist_ok=True)

            image_id = message.photo[-1].file_id
            image_name = "{0}.jpg".format(image_id)

            logger.info("Got image from {0} --- Image: {1}\n".format(message.chat.username, image_name))

            image_info = bot.get_file(image_id)
            downloaded_image = bot.download_file(image_info.file_path)

            image = open("{0}/{1}".format(storage_path, image_name), 'wb')
            image.write(downloaded_image)
            image.close()

            logger.info("Starting image processing. --- Image: {0}\n".format(image_name))

            out = process_image(image_name)

            bot.send_message(chat_id=message.chat.id, text=out, reply_to_message_id=message.message_id)

        except Exception as e:
            logger.error("ExceptionFromPhoto {0}: ".format(image_name) + str(e))
            pass

    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as ex:
            logger.error("Global Exception: " + str(ex))
            time.sleep(15)

except Exception as ex:
    logger.error("Global Exception: " + str(ex))
