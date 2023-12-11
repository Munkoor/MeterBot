from aiogram.filters.callback_data import CallbackData


class LanguageCallbackData(CallbackData, prefix="lang"):
    langauage_code: str


class AddressCallbackData(CallbackData, prefix="addr"):
    address: str




