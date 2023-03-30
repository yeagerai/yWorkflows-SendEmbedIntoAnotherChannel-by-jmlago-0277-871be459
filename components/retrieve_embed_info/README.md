
# RetrieveEmbedInfo

Takes the input URL and extracts the required information to generate the Discord embed card message for the Discord repository.

## Initial generation prompt
description: Takes the input URL and extracts the required information to generate
  the Discord embed card message for the Discord repository.
inputs_from_previous_nodes: None
name: RetrieveEmbedInfo


## Transformer breakdown
- Retrieve the page content from the input URL.
- Parse the page content using an appropriate parser.
- Extract the required information such as title, description, image etc.
- Check if the information is within the character limits for Discord embed usage.
- Format the extracted information into a structured dictionary.
- Return the formatted discord embed_info.

## Parameters
[{'default_value': 10, 'description': 'The maximum time to wait for a response from the input URL before raising an exception.', 'name': 'timeout', 'type': 'int'}]

        