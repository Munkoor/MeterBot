from aiogram import Router
from aiogram.types import CallbackQuery

from callback_data import LanguageCallbackData

router = Router()


@router.callback_query(LanguageCallbackData.filter())
async def select_language_query(
    callback_query: CallbackQuery, callback_data: LanguageCallbackData
) -> None:
    await callback_query.message.answer(
        f"Your language is {callback_data.langauage_code}"
    )
    await callback_query.answer()
