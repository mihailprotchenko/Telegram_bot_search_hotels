from loader import bot
from states.history import HistoryStates
from telebot.types import InputMediaPhoto
from keyboards.inline.find_hotel import photos_slider
from telebot.apihelper import ApiTelegramException


@bot.callback_query_handler(state=HistoryStates.result_with_pic_state, func=None)
def show_hotel_photo(call):
    # При нажатии на числовую кнопку пагинатора
    hotel_id, photo_index = call.data.split('_')
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        photos = data[f"images_of_{hotel_id}"]
    # Правим сообщение
    # Используется когда нажали на числовую кнопку в пагинаторе
    try:
        bot.edit_message_media(chat_id=call.message.chat.id,
                               message_id=call.message.message_id,
                               media=InputMediaPhoto(photos[int(photo_index) - 1],
                                                     caption=data[f"caption_of_{hotel_id}"]),
                               # Передаем класс InputMediaPhoto для замены фотографии
                               reply_markup=photos_slider.markup(len(photos), page=int(photo_index), hotelid=hotel_id)
                               )
    except ApiTelegramException:
        bot.answer_callback_query(call.id, "Загружаю другую картинку подождите, попробуйте позже.", show_alert=False)
