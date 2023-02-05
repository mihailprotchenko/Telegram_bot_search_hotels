from telebot.types import Message
from loader import bot
from states.edit import EditStates
from states.find_hotel import FindHotelState
from states.history import HistoryStates


# Эхо хендлер, куда летят некорректные текстовые сообщения в процессе выполнения команд


@bot.message_handler(state=[el.__getattribute__(el, state) for el in [EditStates, FindHotelState, HistoryStates]
                            for state in dir(el) if state.endswith('_state')],
                     func=lambda message: not message.text.startswith('/'))
def incorrect_input(message: Message) -> None:
    bot.reply_to(message, "Пожалуйста выберите предложенный вариант")
