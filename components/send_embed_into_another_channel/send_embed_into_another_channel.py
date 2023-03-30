
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class SendEmbedIntoAnotherChannelInput(BaseModel):
    url: str
    discord_channel_id: str


class SendEmbedIntoAnotherChannelOutput(BaseModel):
    embed_message_sent: bool


class SendEmbedIntoAnotherChannel(AbstractWorkflow):

    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: SendEmbedIntoAnotherChannelInput, callbacks: typing.Any
    ) -> SendEmbedIntoAnotherChannelOutput:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        embed_message_sent = results_dict['embed_message_sent'].value
        out = SendEmbedIntoAnotherChannelOutput(embed_message_sent=embed_message_sent)
        return out


load_dotenv()
send_embed_into_another_channel_app = FastAPI()


@send_embed_into_another_channel_app.post("/transform/")
async def transform(
    args: SendEmbedIntoAnotherChannelInput,
) -> SendEmbedIntoAnotherChannelOutput:
    send_embed_into_another_channel = SendEmbedIntoAnotherChannel()
    return await send_embed_into_another_channel.transform(args, callbacks=None)

