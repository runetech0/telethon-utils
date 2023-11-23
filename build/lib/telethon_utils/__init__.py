from typing import Never
from telethon import events # pyright: ignore



def stop_event() -> Never:
    raise events.StopPropagation