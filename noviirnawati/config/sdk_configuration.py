import os

from google.genai.types import SafetySetting, HarmCategory, HarmBlockThreshold

# Gen AI Client
GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT')
GOOGLE_CLOUD_LOCATION = os.getenv('GOOGLE_CLOUD_LOCATION')
GOOGLE_GENAI_USE_VERTEXAI = os.getenv('GOOGLE_GENAI_USE_VERTEXAI')
GOOGLE_GENAI_MODEL_TYPE = os.getenv('GOOGLE_GENAI_MODEL_TYPE')
GOOGLE_GENAI_API_VERSION = os.getenv('GOOGLE_GENAI_API_VERSION')

# Gen AI Generate Content Parameters
GOOGLE_GENAI_SYSTEM_INSTRUCTION = os.getenv('GOOGLE_GENAI_SYSTEM_INSTRUCTION')
GOOGLE_GENAI_TEMPERATURE = os.getenv('GOOGLE_GENAI_TEMPERATURE')
GOOGLE_GENAI_TOP_P = os.getenv('GOOGLE_GENAI_TOP_P')
GOOGLE_GENAI_TOP_K = os.getenv('GOOGLE_GENAI_TOP_K')
GOOGLE_GENAI_SAFETY_SETTINGS = [
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
]
