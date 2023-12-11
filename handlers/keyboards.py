from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_data import LanguageCallbackData, AddressCallbackData


def select_language_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="en", callback_data=LanguageCallbackData(langauage_code="en"))
    builder.button(text="ua", callback_data=LanguageCallbackData(langauage_code="ua"))
    return builder.as_markup()


def select_address_keyboard(addresses: list[str]):
    builder = InlineKeyboardBuilder()

    for address in addresses:
        builder.button(text=address, callback_data=AddressCallbackData(address=address))
    
    return builder.as_markup()
