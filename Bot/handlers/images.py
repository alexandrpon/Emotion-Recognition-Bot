from aiogram import Router, F, Bot
from aiogram.types import Message, PhotoSize, InputMediaPhoto, FSInputFile
from aiogram.enums.input_media_type import InputMediaType
from ML.Emotion_Recognition.predict import emo_rec_pred
import os


router = Router()


@router.message(F.photo[-1].as_("largest_photo"))
async def img_handler(message: Message, largest_photo: PhotoSize, bot: Bot):
    photo_id = largest_photo.file_id
    disk_path = "ML\Emotion_Recognition\images/" + str(photo_id) + ".jpg"
    await bot.download(file=photo_id, destination=disk_path)
    emotion = await emo_rec_pred(disk_path)

    media = [
        InputMediaPhoto(type=InputMediaType.PHOTO, media=photo_id, caption="Оригинал"),
        InputMediaPhoto(
            type=InputMediaType.PHOTO,
            media=FSInputFile(disk_path),
            caption="Реплика",
        ),
    ]
    await message.answer_media_group(media=media)
    await message.answer(f"Эмоция: {emotion}")

    os.remove(disk_path)
