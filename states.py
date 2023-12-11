from aiogram.fsm.state import StatesGroup, State


class MeterForm(StatesGroup):
    address = State()
    value = State()
    photo = State()