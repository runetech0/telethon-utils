# pyright: basic
from typing import Optional, cast
from telethon import TelegramClient
from telethon.types import Message as TelegramMessage, UpdateNewMessage, PeerUser
from telethon.events import NewMessage
from telethon.events.common import EventCommon


def std_chat_id(chat_id: int) -> int:
    _id = str(chat_id)
    if _id.startswith("-100"):
        _id = _id[3:]

    if _id.startswith("-"):
        _id = _id[1:]

    return int(_id)


def get_message_obj_from_message_event(event: NewMessage.Event) -> TelegramMessage:
    """Extract typed message object from TelegramMessage"""
    orig_update = cast(UpdateNewMessage, event.original_update)
    return cast(TelegramMessage, orig_update.message)


def get_user_id_from_message_event(event: NewMessage.Event) -> Optional[int]:
    pure_message = get_message_obj_from_message_event(event)
    if isinstance(pure_message.peer_id, PeerUser):
        return pure_message.peer_id.user_id

    return None


def get_client_from_event(event: EventCommon) -> TelegramClient:
    return cast(TelegramClient, event.client)
