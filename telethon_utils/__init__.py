from typing import Never
from telethon import events # pyright: ignore
from .rich_client import *
from .emojis import *


def stop_event() -> Never:
    raise events.StopPropagation