import os

from google.genai.types import SafetySetting, HarmCategory, HarmBlockThreshold

# Gen AI Client
GOOGLE_CLOUD_API_KEY: str = os.getenv('GOOGLE_CLOUD_API_KEY', '')
GOOGLE_GENAI_MODEL_TYPE: str = os.getenv('GOOGLE_GENAI_MODEL_TYPE', 'gemini-2.0-flash-001')

# Gen AI Generate Content Parameters
GOOGLE_GENAI_BASE_PROMPT: str = os.getenv('GOOGLE_GENAI_BASE_PROMPT', '')
GOOGLE_GENAI_SYSTEM_INSTRUCTION: str = os.getenv('GOOGLE_GENAI_SYSTEM_INSTRUCTION', '')
GOOGLE_GENAI_TEMPERATURE: float = os.getenv('GOOGLE_GENAI_TEMPERATURE', 1.0)
GOOGLE_GENAI_TOP_P: float = os.getenv('GOOGLE_GENAI_TOP_P', 0.8)
GOOGLE_GENAI_TOP_K: int = os.getenv('GOOGLE_GENAI_TOP_K', 30)
GOOGLE_GENAI_SAFETY_SETTINGS: list[SafetySetting] = [
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

if len(GOOGLE_CLOUD_API_KEY) == 0:
    raise EnvironmentError('Environment variable GOOGLE_CLOUD_API_KEY must be provided')
if len(GOOGLE_GENAI_BASE_PROMPT) < 50:
    raise EnvironmentError('Environment variable GOOGLE_GENAI_BASE_PROMPT must be provided')
if len(GOOGLE_GENAI_SYSTEM_INSTRUCTION) < 50:
    raise EnvironmentError('Environment variable GOOGLE_GENAI_SYSTEM_INSTRUCTION must be provided')
