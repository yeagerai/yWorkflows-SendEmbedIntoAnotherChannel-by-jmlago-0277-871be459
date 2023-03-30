
import pytest
from pydantic import ValidationError
from unittest.mock import AsyncMock, MagicMock

from component.prepare_and_send_embed_message import PrepareAndSendEmbedMessage, PrepareAndSendEmbedMessageInputDict, PrepareAndSendEmbedMessageOutputDict

# 1. Define test cases with mocked input and expected output data.
mocked_data = [
    (
        {
            "embed_info": {
                "title": "Test Title",
                "description": "Test Description",
                "color": 0x123456,  # Replace with an actual color code
                "fields": [
                    {"name": "Field 1", "value": "Value 1"},
                    {"name": "Field 2", "value": "Value 2"},
                ],
            }
        },
        {"embed_message_sent": True},
    ),
    (
        {
            "embed_info": {
                "title": "Test Title",
                "description": "Test Description",
                "color": 0x123456,  # Replace with an actual color code
                "fields": [],
            }
        },
        {"embed_message_sent": True},
    ),
    (
        {"embed_info": {}},
        ValidationError,
    ),
]

# 2. Use @pytest.mark.parametrize to create multiple test scenarios.
@pytest.mark.parametrize("input_data,expected_output", mocked_data)
@pytest.mark.asyncio
async def test_prepare_and_send_embed_message_transform(input_data, expected_output):
    # 3. Write a test function that takes the mocked input,
    # calls the component's transform() method, and asserts that the
    # output matches the expected output.

    component = PrepareAndSendEmbedMessage()

    # Mock the discord.Client methods
    component.client = AsyncMock()
    component.client.start = AsyncMock()
    component.client.close = AsyncMock()

    # 4. Include error handling and edge case scenarios, if applicable.
    if expected_output is ValidationError:
        with pytest.raises(expected_output):
            input_dict = PrepareAndSendEmbedMessageInputDict(**input_data)
    else:
        input_dict = PrepareAndSendEmbedMessageInputDict(**input_data)
        output_dict = await component.transform(input_dict)

         # Assert that the output matches the expected output
        assert output_dict.dict() == expected_output

        # Assert mocks have been called
        component.client.start.assert_called()
        component.client.close.assert_called()
