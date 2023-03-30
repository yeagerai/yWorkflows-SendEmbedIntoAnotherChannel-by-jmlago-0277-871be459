
import os
import yaml
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class RetrieveEmbedInfoInput(BaseModel):
    url: str


class RetrieveEmbedInfoOutput(BaseModel):
    embed_info: dict


class RetrieveEmbedInfo(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.timeout: int = yaml_data["parameters"]["timeout"]

    def transform(self, args: RetrieveEmbedInfoInput) -> RetrieveEmbedInfoOutput:
        response = requests.get(args.url, timeout=self.timeout)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.title.string if soup.title else ""
        description = soup.find("meta", attrs={"name": "description"})
        description = description["content"] if description else ""

        image = soup.find("meta", property="og:image")
        image = image["content"] if image else ""

        embed_info = {
            "title": title,
            "description": description,
            "image": {"url": image},
            "url": args.url
        }

        return RetrieveEmbedInfoOutput(embed_info=embed_info)


load_dotenv()
retrieve_embed_info_app = FastAPI()


@retrieve_embed_info_app.post("/transform/")
async def transform(args: RetrieveEmbedInfoInput) -> RetrieveEmbedInfoOutput:
    retrieve_embed_info = RetrieveEmbedInfo()
    return retrieve_embed_info.transform(args)

