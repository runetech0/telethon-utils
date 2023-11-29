from telethon.tl.custom import Button
from telethon.events import CallbackQuery
from telethon.types import KeyboardButtonCallback
from telethon.tl.custom import Button




def data_button(text: str, data: bytes | str) -> KeyboardButtonCallback:
    if isinstance(data, str):
        data = data.encode()
    return Button.inline(text=text, data=data)


def join_query(prefix: str, data: str) -> str:
    return f"{prefix}:{data}"


def split_query(data: str) -> list[str]:
    return data.split(":")


def extract_query_data(e: CallbackQuery.Event, remove_prefix: bool = True) -> str:
    data = e.query.data.decode()
    if remove_prefix:
        return split_query(data)[-1]
    return data
