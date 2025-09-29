import os.path
import traceback

from google import genai
from google.genai import Client
from google.genai.types import GenerateContentConfig, GenerateContentResponse

from ..config.base_configuration import AI_ANALYSIS_SAVED_AS_MARKDOWN
from ..config.sdk_configuration import (GOOGLE_GENAI_MODEL_TYPE,
                                        GOOGLE_GENAI_BASE_PROMPT,
                                        GOOGLE_GENAI_SYSTEM_INSTRUCTION,
                                        GOOGLE_GENAI_TEMPERATURE,
                                        GOOGLE_GENAI_TOP_K,
                                        GOOGLE_GENAI_TOP_P,
                                        GOOGLE_GENAI_SAFETY_SETTINGS, GOOGLE_CLOUD_API_KEY)
from ..constant.constant import Generic
from ..helper import str_utility
from ..helper.validator import str_is_empty_or_none
from ..helper.writer import write_output_to_markdown
from ..model.model import PlaylistItem


def build_prompt(songs_collections: list[PlaylistItem]) -> str:
    if len(songs_collections) == 0: return Generic.EMPTY_STRING
    prompt = "Playlist Data (Semicolon-separated list: Song Title - Artist; Song Title - Artist, ...):"

    for song in songs_collections:
        prompt += Generic.WHITESPACE
        prompt += song.title
        prompt += " - "
        prompt += song.artist
        prompt += ";"

    return prompt


def construct_markdown_filename(url: str) -> str:
    return os.path.join("output_result-" + str_utility.extract_playlist_id(url))


def ai_analysis_google(prompt_context: str) -> str:
    client: Client = genai.Client(api_key=GOOGLE_CLOUD_API_KEY)
    print("Generate GenAI Client")

    print("Begin generating content")
    response: GenerateContentResponse = client.models.generate_content(
        model=GOOGLE_GENAI_MODEL_TYPE,
        contents=[GOOGLE_GENAI_BASE_PROMPT, prompt_context],
        config=GenerateContentConfig(
            system_instruction=GOOGLE_GENAI_SYSTEM_INSTRUCTION,
            temperature=GOOGLE_GENAI_TEMPERATURE,
            top_p=GOOGLE_GENAI_TOP_P,
            top_k=GOOGLE_GENAI_TOP_K,
            safety_settings=GOOGLE_GENAI_SAFETY_SETTINGS
        ))
    print("Finished generating content")
    client.close()
    print("Closing GenAI Client")
    return response.text


def ai_analysis(song_collections: list, url: str):
    try:
        prompt_context = build_prompt(song_collections)
        if str_is_empty_or_none(prompt_context): raise AssertionError("No prompt context")

        # TODO: try multiple SDK provider besides google, create a switch case, choose the provider based on the environment variable
        response = ai_analysis_google(prompt_context)

        # save as markdown only if the environment variables say so
        if AI_ANALYSIS_SAVED_AS_MARKDOWN:
            write_output_to_markdown("result", str_utility.extract_playlist_id(url), response)

        print("\n\n\nPrinting generated response\n\n\n")
        print(response)
        print("\n\n\nFinished printing generated response\n\n\n")
        return response

    except Exception:
        traceback.print_exc()
        response = "No Result, please try again with a different URL"
        print(response)
        return response
