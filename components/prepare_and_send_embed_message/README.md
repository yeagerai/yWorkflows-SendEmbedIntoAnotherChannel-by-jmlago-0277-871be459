
# PrepareAndSendEmbedMessage

Accepts the extracted information, prepares an embed message based on that info, and sends it to the given Discord channel or thread.

## Initial generation prompt
description: Accepts the extracted information and prepares the embed message based
  on that info. Then, sends it to the given Discord channel or thread.
inputs_from_previous_nodes:
- embed_info: RetrieveEmbedInfo
name: PrepareAndSendEmbedMessage


## Transformer breakdown
- Initialize Discord client with the given API token
- Prepare an embed message using the information from the input_dict
- Send the embed message to the specified Discord channel or thread
- Return True if the message was sent successfully, otherwise return False

## Parameters
[{'default_value': 'None', 'description': 'The ID of the Discord channel or thread where the message will be sent.', 'name': 'discord_channel_id', 'type': 'str'}, {'default_value': 'None', 'description': 'The API token for accessing the Discord server to send the message.', 'name': 'discord_api_token', 'type': 'str'}]

        