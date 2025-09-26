import os.path
from datetime import date

from google import genai
from google.genai.types import HttpOptions, GenerateContentConfig

from ..config.base_configuration import AI_ANALYSIS_SAVED_AS_MARKDOWN
from ..config.sdk_configuration import (GOOGLE_GENAI_MODEL_TYPE,
                                        GOOGLE_GENAI_API_VERSION,
                                        GOOGLE_CLOUD_PROJECT,
                                        GOOGLE_CLOUD_LOCATION,
                                        GOOGLE_GENAI_USE_VERTEXAI,
                                        GOOGLE_GENAI_SYSTEM_INSTRUCTION,
                                        GOOGLE_GENAI_TEMPERATURE,
                                        GOOGLE_GENAI_TOP_K,
                                        GOOGLE_GENAI_TOP_P,
                                        GOOGLE_GENAI_SAFETY_SETTINGS)
from ..constant.constant import Generic
from ..helper.validator import str_is_empty_or_none
from ..helper.writer import write_output_to_markdown


def build_prompt(songs_collections: list) -> str:
    if len(songs_collections) == 0: return Generic.EMPTY_STRING
    return "TODO"  # TODO EXPERIMENT ON GEMINI


def construct_markdown_filename(url: str) -> str:
    splitted_url = url.split("/")
    return os.path.join("output_result-" + splitted_url[
        len(splitted_url) - 1] + "-" + date.today().strftime("%y%m%d"))


def ai_analysis_google(prompt: str) -> str:
    client = genai.Client(vertexai=GOOGLE_GENAI_USE_VERTEXAI, project=GOOGLE_CLOUD_PROJECT,
                          location=GOOGLE_CLOUD_LOCATION,
                          http_options=HttpOptions(api_version=GOOGLE_GENAI_API_VERSION))

    response = Generic.EMPTY_STRING
    for chunk in client.models.generate_content_stream(
            model=GOOGLE_GENAI_MODEL_TYPE,
            contents=prompt,
            config=GenerateContentConfig(
                system_instruction=GOOGLE_GENAI_SYSTEM_INSTRUCTION,
                temperature=GOOGLE_GENAI_TEMPERATURE,
                top_p=GOOGLE_GENAI_TOP_P,
                top_k=GOOGLE_GENAI_TOP_K,
                safety_settings=GOOGLE_GENAI_SAFETY_SETTINGS
            )):
        print(chunk.text)
        response += chunk.text
    return response


def ai_analysis(song_collections: list, url: str):
    try:
        prompt = build_prompt(song_collections)
        if str_is_empty_or_none(prompt): return "No Results"

        # TODO: try multiple SDK provider besides google, create a switch case, choose the provider based on the environment variable
        response = ai_analysis_google(prompt)

        # save as markdown only if the environment variables say so
        if AI_ANALYSIS_SAVED_AS_MARKDOWN:
            write_output_to_markdown(construct_markdown_filename(url), response)

        return response
    except Exception:
        return "No Result, please try again with a different URL"
