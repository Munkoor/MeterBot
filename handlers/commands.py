import datetime
import os.path
import uuid

from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart

import handlers.keyboards as kb
from googledrive import upload_photo
from states import MeterForm
from callback_data import AddressCallbackData
from googlesheets import write_dictionary_to_sheet

router = Router()


addresses = [
    "Lvlv, 12 Chornovola St.",
    "Kyiv, 23 Shevchenko St.",
    "Kharkiv, 102 Ivan Franko St.",
]


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}! I am a Telegram bot that helps you easily and conveniently enter meter readings into Google Sheets and photos of meters in Google Drive. To get started, write <b>/meter</b> in chat")


@router.message(Command("select_language"))
async def select_language_command(message: Message) -> None:
    await message.answer(
        "Select a language.",
        reply_markup=kb.select_language_keyboard()
    )


@router.message(Command("cancel"))
async def cancel_command(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()
    await message.answer("Cancelled.")


@router.message(Command("meter"))
async def meter_command(message: Message, state: FSMContext):
    await state.set_state(MeterForm.address)
    await message.answer("Select an address.", reply_markup=kb.select_address_keyboard(addresses))


@router.callback_query(MeterForm.address, AddressCallbackData.filter())
async def meter_select_address_query(query: CallbackQuery, callback_data: AddressCallbackData, state: FSMContext):
    await state.set_state(MeterForm.value)
    await state.update_data({"username": query.from_user.full_name})
    await state.update_data({"addr": callback_data.address})
    await query.message.answer("Enter meter value.")
    await query.answer()


@router.message(MeterForm.value, F.text.isnumeric())
async def meter_enter_value_handler(message: Message, state: FSMContext):
    await state.set_state(MeterForm.photo)
    await state.update_data({"value": message.text})
    await message.answer("Send a photo of the water meter.")


@router.message(MeterForm.photo, F.content_type == "photo")
async def meter_send_photo_handler(message: Message, bot: Bot,  state: FSMContext):
    file = await bot.get_file(message.photo[-1].file_id)

    photo_full_name = os.path.join("meters_photo", f"{message.from_user.username}_meter-{uuid.uuid4()}.jpg")

    await bot.download_file(file.file_path, photo_full_name)
    upload_photo("photos-of-meters.json", photo_full_name, f"{message.from_user.username}_meter-{datetime.date.today()}.jpg", os.getenv("GOOGLE_DRIVE_TOKEN"))

    await message.answer("Record saved.")
    write_dictionary_to_sheet(await state.get_data())
    print(await state.get_data())
    await state.clear()
