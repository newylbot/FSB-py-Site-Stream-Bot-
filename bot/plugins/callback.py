from hydrogram.types import CallbackQuery
from bot import TelegramBot
from bot.modules.decorators import verify_user
from bot.modules.static import *
from bot.modules.telegram import get_message, parse_caption_meta

@TelegramBot.on_callback_query()
@verify_user
async def manage_callback(bot, q: CallbackQuery):
    query = q.data

    if query.startswith('rm_'):
        parts = query.split('_')

        if len(parts) != 3:
            return await q.answer(InvalidQueryText, show_alert=True)

        message = await get_message(int(parts[1]))

        if not message:
            return await q.answer(MessageNotExist, show_alert=True)
        
        stored_code, user_id = parse_caption_meta(message.caption)

        if q.from_user.id != user_id or parts[2] != stored_code:
            return await q.answer(InvalidQueryText, show_alert=True)
        
        await message.delete()
        await q.answer(LinkRevokedText, show_alert=True)
    else:
        await q.answer(InvalidQueryText, show_alert=True)
