from typing import Optional
from telethon import TelegramClient # pyright: ignore
from telethon import types, functions  # pyright: ignore




class RichTelegramClient(TelegramClient):
    

    me: Optional[types.User]
    phone_number: str

    # private attrs
    _rich_init_done: bool = False

    async def rich_init(self) -> None:
        if not self._rich_init_done:
            self._rich_init_done = True
            me = await self.get_me()
            assert isinstance(me, types.User)
            self.me = me

    @property
    def user_id(self) -> int:
        assert self.me, "Client User not available"
        return self.me.id

    @property
    def repr(self) -> str:
        """Something that can be represented on terminal"""
        if self.me:
            if self.me.username:
                return "@" + self.me.username

            if self.me.phone:
                return self.me.phone

            if self.me.first_name:
                return self.me.first_name

        return ""

    def link_to_slug(self, link: str) -> str:
        return link.split("/")[-1].replace("@", "").replace("+", "")

    async def check_chat_invite_link(self, link: str) -> types.ChatInviteAlready | types.ChatInvite:
        result = await self(functions.messages.CheckChatInviteRequest(  # pyright: ignore
            hash=self.link_to_slug(link)
        ))
        assert isinstance(result, (types.ChatInviteAlready, types.ChatInvite))
        return result

    async def join_public_entity(self, entity_slug: str) -> None:
        """Join a public channel or group"""
        entity_slug = self.link_to_slug(entity_slug)
        await self(functions.channels.JoinChannelRequest(entity_slug))  # pyright: ignore

    async def join_private_entity(self, entity_slug: str) -> None:
        entity_slug = self.link_to_slug(entity_slug)
        await self(functions.messages.ImportChatInviteRequest(entity_slug))

    async def is_private_entity_link(self, link: str) -> bool:
        if "joinchat" in link:
            return True
        return link.split("/")[-1].replace("@", "").startswith("+")

    async def join_entity(self, entity_link: str) -> None:
        if await self.is_private_entity_link(entity_link):
            await self.join_private_entity(entity_link)

        else:
            await self.join_public_entity(entity_link)
