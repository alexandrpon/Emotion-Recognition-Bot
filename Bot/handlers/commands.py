from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from Bot.queries.users import add_id_to_bd

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await add_id_to_bd(message.from_user.id)
    await message.answer("Hi")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("I can recognize face emotion if you send me a image")
