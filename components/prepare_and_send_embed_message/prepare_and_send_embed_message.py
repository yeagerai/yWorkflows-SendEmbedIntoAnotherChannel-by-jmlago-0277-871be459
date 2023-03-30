
import os
from typing import Dict

import discord
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class PrepareAndSendEmbedMessageInputDict(BaseModel):
    embed_info: Dict


class PrepareAndSendEmbedMessageOutputDict(BaseModel):
    embed_message_sent: bool


class PrepareAndSendEmbedMessage(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.discord_channel_id: str = os.environ.get(
            yaml_data["parameters"]["discord_channel_id"]
        )
        self.discord_api_token: str = os.environ.get(
            yaml_data["parameters"]["discord_api_token"]
        )

    async def transform(
        self, args: PrepareAndSendEmbedMessageInputDict
    ) -> PrepareAndSendEmbedMessageOutputDict:

        embed_info = args.embed_info
        client = discord.Client()

        def prepare_embed(embed_data: Dict):
            embed = discord.Embed(
                title=embed_data["title"],
                description=embed_data["description"],
                color=embed_data["color"],
            )
            for field in embed_data["fields"]:
                embed.add_field(name=field["name"], value=field["value"], inline=False)
            return embed

        async def send_embed(embed: discord.Embed):
            await client.login(self.discord_api_token)
            channel = await client.fetch_channel(self.discord_channel_id)
            await channel.send(embed=embed)

        async def on_ready():
            embed = prepare_embed(embed_info)
            await send_embed(embed)
            await client.close()

        client.on_ready = on_ready

        try:
            await client.start()
            return PrepareAndSendEmbedMessageOutputDict(
                embed_message_sent=True
            )
        except Exception as e:
            print(f"Error sending embed message: {e}")
            return PrepareAndSendEmbedMessageOutputDict(
                embed_message_sent=False
            )


load_dotenv()
prepare_and_send_embed_message_app = FastAPI()


@prepare_and_send_embed_message_app.post("/transform/")
async def transform(
    args: PrepareAndSendEmbedMessageInputDict,
) -> PrepareAndSendEmbedMessageOutputDict:
    prepare_and_send_embed_message = PrepareAndSendEmbedMessage()
    return await prepare_and_send_embed_message.transform(args)
