import base64
from dotenv import load_dotenv
from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize models
prompt_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite"
)
image_model = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash-preview-image-generation"
)

# Thumbnail prompt template
prompt_template = PromptTemplate(
    input_variables=["video_summary"],
    template="""Create a prompt to generate a youtube thumbnail based on given youtube summary / transcript. 
{video_summary}
"""
)

def generate_thumbnail_prompt(video_summary: str) -> str:
    formatted_prompt = prompt_template.format(video_summary=video_summary)
    result = prompt_model.invoke(formatted_prompt)
    return result.content

def generate_image(prompt: str) -> bytes:
    response = image_model.invoke(
        [prompt],
        generation_config=dict(response_modalities=["TEXT", "IMAGE"]),
    )
    return decode_image(response)

def decode_image(response: AIMessage) -> bytes:
    image_block = next(
        block
        for block in response.content
        if isinstance(block, dict) and block.get("image_url")
    )
    image_base64 = image_block["image_url"]["url"].split(",")[-1]
    return base64.b64decode(image_base64)
