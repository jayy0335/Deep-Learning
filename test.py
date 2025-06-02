# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
    api_key = "AIzaSyDVUs7IYvroEqzWmrRY3QmqZu_oCrTK1Ok"
        )

    model = "gemini-1.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is here"""),
            ],
        ),
    ]
    # tools = [
    #     types.Tool(googleSearchRetrieval=types.DynamicRetrievalConfig(dynamicThreshold=0.3, mode=types.DynamicRetrievalConfigMode.MODE_DYNAMIC)),
    # ]
    # generate_content_config = types.GenerateContentConfig(
    #     tools=tools,
    #     response_mime_type="text/plain",
    # )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        # config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
