from croydon.models.storable_model import StorableModel
from croydon.models.fields import ReferenceField, StringField
from croydon.models.reference import OnDestroy
from .chat import Chat


class Subscription(StorableModel):

    COLLECTION = "subscriptions"

    chat_id: ReferenceField[Chat] = ReferenceField(reference_model=Chat, on_destroy=OnDestroy.CASCADE)
    query = StringField(required=True)

    async def chat(self) -> Chat:
        return await Chat.get(self.chat_id)
