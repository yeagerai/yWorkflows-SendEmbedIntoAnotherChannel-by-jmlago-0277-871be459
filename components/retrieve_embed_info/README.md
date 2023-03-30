markdown
# Component Name

RetrieveEmbedInfo

# Description

The `RetrieveEmbedInfo` component is a building block of a Yeager Workflow designed to retrieve relevant metadata from a given URL, such as the title, description, and image. This info can be used to create a rich media preview for the URL, similar to what social media platforms display when sharing links.

# Input and Output Models

The component uses Pydantic's BaseModel for data validation and serialization. The input and output models are defined as follows:

## Input Model

- `url` (str): The target web page URL from which to retrieve the embed information.

## Output Model

- `embed_info` (dict): A dictionary containing the extracted embed information, including the following keys:
  - `title` (str): The page's title.
  - `description` (str): The page's description.
  - `image` (dict): A dictionary containing the `url` (str) of the image, if it exists.
  - `url` (str): The input web page URL.

# Parameters

The component uses a configuration file in YAML format to define required parameters. The parameters are:

- `timeout` (int): The request timeout duration in seconds. Set in the component's configuration file.

# Transform Function

The `transform()` method processes the input data and retrieves embed metadata from a given URL. Its implementation can be broken down into the following steps:

1. Send an HTTP GET request to the specified `url` using the `requests` library, with the configured `timeout` duration.
2. Raise an exception if the requested URL returns an error status.
3. Parse the content of the HTTP response using `BeautifulSoup`.
4. Extract the page title, description, and image information from the parsed content.
5. Construct a dictionary `embed_info` containing the extracted metadata.
6. Return an instance of the `RetrieveEmbedInfoOutput` model containing the `embed_info` dictionary.

# External Dependencies

The component relies on the following external libraries:

- `requests`: For sending HTTP requests to web pages.
- `BeautifulSoup`: For parsing and extracting data from HTML content.
- `Pydantic`: For input and output data validation and serialization.
- `yaml`: For parsing the component's configuration file.

# API Calls

The component makes external GET requests to the provided URL to retrieve its HTML content. It does not rely on any specific API other than the target web page's content.

# Error Handling

The component raises an exception if the requested URL returns an error status. This is handled using the `raise_for_status()` method from the `requests` library.

# Examples

Let's assume, you have the following configuration file `retrieve_embed_info.yaml`:

