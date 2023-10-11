from typing import TYPE_CHECKING
from croydon.models.storable_model import StorableModel
from croydon.db import ObjectsCursor
from croydon.models.fields import StringField
if TYPE_CHECKING:
    from .subscription import Subscription


class Chat(StorableModel):

    COLLECTION = "chats"
    KEY_FIELD = "chat_id"

    chat_id = StringField(required=True)
    first_name = StringField()
    last_name = StringField()
    username = StringField()
    chat_type = StringField()

    def subscriptions(self) -> ObjectsCursor["Subscription"]:
        from .subscription import Subscription
        return Subscription.find({"chat_id": self.id})
