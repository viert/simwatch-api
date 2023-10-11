from pydantic import BaseModel
from typing import List, Optional


class FromField(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str


class ChatField(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    type: str


class Entity(BaseModel):
    offset: int
    length: int
    type: str
    text: Optional[str] = None


class Message(BaseModel):
    message_id: int
    from_: FromField
    chat: ChatField
    date: int
    text: str
    entities: Optional[List[Entity]]

    def get_entity(self, idx: int) -> Optional[Entity]:
        if self.entities is None:
            return None
        ent = self.entities[idx]
        ent.text = self.text[ent.offset:ent.offset+ent.length]
        return ent

    def commands(self) -> Optional[List[Entity]]:
        if self.entities is None:
            return None
        ents = [self.get_entity(idx) for idx in range(len(self.entities))]
        ents = [ent for ent in ents if ent.type == "bot_command"]
        return ents

    def command(self) -> Optional[Entity]:
        cmds = self.commands()
        if cmds is None or len(cmds) != 1:
            return None
        return cmds[0]

    class Config:
        fields = {
            "from_": "from"
        }
