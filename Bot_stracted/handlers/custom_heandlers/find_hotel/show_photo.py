from loader import bot
from states.find_hotel import FindHotelState
from telebot.types import InputMediaPhoto
from keyboards.inline.find_hotel import photos_slider
from telebot.apihelper import ApiTelegramException
from telebot.types import CallbackQuery


@bot.callback_query_handler(state=[FindHotelState.send_result_with_photo_state], func=None)
def show_hotel_photo(call: CallbackQuery) -> None:
    """Обработчик нажатия на кнопку пагинатора, для загрузки новой фотографии"""
    hotel_id, photo_index = call.data.split('_')
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        photos = data['api_data'][f"images_of_{hotel_id}"]
    # Правим сообщение
    # Используется когда нажали на числовую кнопку в пагинаторе
    try:
        bot.edit_message_media(chat_id=call.message.chat.id,
                               message_id=call.message.message_id,
                               media=InputMediaPhoto(photos[int(photo_index) - 1],
                                                     caption=data['api_data'][f"caption_of_{hotel_id}"]),
                               # Передаем класс InputMediaPhoto для замены фотографии
                               reply_markup=photos_slider.markup(len(photos), page=int(photo_index), hotelid=hotel_id)
                               )
    except ApiTelegramException:
        bot.answer_callback_query(call.id, "Загружаю другую картинку подождите, попробуйте позже.", show_alert=False)
