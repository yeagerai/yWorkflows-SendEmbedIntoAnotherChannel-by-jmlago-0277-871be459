
# test_send_embed_into_another_channel.py

import pytest
from typing import Any
from pydantic import BaseModel
from fastapi import FastAPI
from core.workflows.abstract_workflow import AbstractWorkflow
from <path_to_component_file> import SendEmbedIntoAnotherChannel, SendEmbedIntoAnotherChannelInput, SendEmbedIntoAnotherChannelOutput

# Creating mocked test examples
TEST_CASES = [
    {
        "input": SendEmbedIntoAnotherChannelInput(url="https://example.com", discord_channel_id="123456789"),
        "output": SendEmbedIntoAnotherChannelOutput(embed_message_sent=True),
    },
    {
        "input": SendEmbedIntoAnotherChannelInput(url="https://test.com", discord_channel_id="987654321"),
        "output": SendEmbedIntoAnotherChannelOutput(embed_message_sent=False),
    },
]

# Using pytest.parametrize to create multiple test scenarios
@pytest.mark.parametrize("test_case", TEST_CASES)
def test_send_embed_into_another_channel_transform(test_case):
    # Initialize the component
    send_embed = SendEmbedIntoAnotherChannel()

    # Call component's transform() method with mocked input
    output_result = send_embed.transform(test_case["input"], callbacks=None)

    # Asserting that the output matches the expected output
    assert output_result == test_case["output"]

