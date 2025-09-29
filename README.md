# **Project: Spotify Playlist "Dating Red Flag" Analysis**

-----

## **Summary: Integrating Data Scraping with Gen AI**

This is an end-to-end Python project that analyzes a user's Spotify playlist to generate an entertaining "dating red flag" personality analysis.

This project represents the successful **MVP (Minimum Viable Product)** build, which was executed in seven days of focused part-time work to quickly demonstrate core technical proficiency in Python.

The MVP's main objective was to validate a solid, production-ready data pipeline by:
- **Data Acquisition**: Grabbing songs from a public Spotify playlist using customized data scraping techniques (network traffic interception from Web UI).
- **GenAI Integration**: Leveraging the 3rd party API SDK to generate structured, nuanced text.
- **Prompt Engineering**: Crafting the personality analysis by designing an optimal prompt and system instructions to achieve the desired content goal.
- **Pipeline Engineering**: Implementing a complete data flow from unformatted scrape data to final, formatted output.

-----

## **Technology Stack**

- **Generative AI**: This demonstrates direct SDK integration and my skills in prompt engineering, using System
  Instructions, parameter configurations and specific prompt to ensure the output is structured, relevant and reliable.
- **Spotify Web API**: Uses the official Spotify Web API for reliable and efficient data acquisition from playlists.
- **Python 3**: The entire data pipeline and application logic are built using modern Python 3.

-----

## Rationale: Why use the Spotify Web API?

The project has been updated to use the official Spotify Web API for several key benefits:

- **Reliability**: Official API provides stable, well-documented endpoints
- **Performance**: Faster and more efficient than web scraping
- **Rate Limiting**: Built-in rate limiting prevents API abuse
- **Data Quality**: Consistent, structured data format
- **Maintenance**: Less prone to breaking due to UI changes

The previous version used Selenium for web scraping as a learning exercise in dynamic data acquisition and network traffic analysis.

-----

## **How It Works: The Flow**

This is the overall flow of the application:

```
Spotify Playlist ⟶ Spotify Web API ⟶ Data Processing ⟶ AI Model ⟶ Analysis Output
```

1. The application is run with a single command-line argument: the URL of a public Spotify playlist.
2. **Spotify Web API** is used to fetch playlist tracks and metadata directly from Spotify's servers.
3. The API returns structured data containing song titles, artists, and other metadata.
4. The extracted data, along with specific prompts and system instructions, is sent to the GenAI model.
5. The AI model, accessed via the Vertex AI API SDK, generates the personality analysis based on the provided data and
   instructions.
6. The final AI-generated response is saved as a Markdown file, with the filename automatically generated in the format
   `output_result-[spotify_playlist_id]-[yymmdd].md`.
    * **Example:** If the playlist URL is `https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq`, and the analysis
      is run on December 31, 2025, the output file will be named `output_result-7wARwuyCiPRMURGmh6xTLq-251231.md`.

-----

## **Requirements**

You'll need a few things to get started:

* **Python 3** installed on your device
* **Spotify Developer Account:** Create an app at https://developer.spotify.com/dashboard to get your client ID and secret
* **Google Vertex AI API Key and Authentication:** All required environment variables are listed in the
  `Environment Variables` section.
* **Python Modules:** All required modules are listed in the `requirements.txt` file.

-----

## **How to Run**

1. Navigate to the project directory in your terminal: `.../spotify-playlist-dating-redflag-analysis`.

2. Ensure you have gathered all of the requirements on section `Requirements`

3. Run the application as a Python module using the following command:

   ```bash
   python -m noviirnawati.main [your_public_spotify_link]
   ```

4. If you're a PyCharm user, you can also use the pre-configured run configuration file located at
   `.run/run-app.run.xml`. You may need to edit the configuration to match your project's local path. If you need to
   change the playlist the Python script analyzes, you'll need to update the string inside the `value` attribute of the
   `<option name="PARAMETERS"...>` tag, simply replace the current URL (the one that starts
   with https://open.spotify.com/playlist/...) with the new public Spotify playlist link you want the scraper to use for
   the analysis.

-----

## **Project Structure**

* `.run/`: PyCharm run configuration files.
* `docs/`: Additional documentation. You can find samples of prompt, configurations, system instruction, and output
  files of this project.
* `noviirnawati/`: The main Python package.
    * `constant/`: Modules holding constant classes and immutable variables.
    * `env/`: Where credentials are stored. This directory is not uploaded to the repository.
    * `helper/`: Modules that support the project's core logic.
    * `model/`: Modules for data definition classes.
    * `output/`: Contains generated output files from the application,
    * `sdk/`: Modules for implementing the 3rd party SDK and its configurations.
    * `web_scraper/`: Modules dedicated to dynamic data scraping.
* `tests/`: A package for unit tests.
    * ***Note:*** *Unit testing is planned for the future, after the Generative AI exploration is complete.*

-----

## **Configuration & Environment Variables**

This project relies on several environment variables for configuration. Here's a quick look at what they do:

```dotenv
# Spotify API credentials (mandatory)
SPOTIFY_CLIENT_ID=string. mandatory. Spotify app client ID, get yours from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_SECRET=string. mandatory. Spotify app client secret, get yours from https://developer.spotify.com/dashboard

# Google AI credentials (mandatory)
GOOGLE_CLOUD_API_KEY=string. mandatory. API key, get yours from https://aistudio.google.com/app/api-keys
GOOGLE_GENAI_MODEL_TYPE=string. gemini model id. if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 

GOOGLE_GENAI_SYSTEM_INSTRUCTION=string. mandatory. system instruction of ai model.
GOOGLE_GENAI_BASE_PROMPT=string. mandatory. prompt for the ai model to generate content.
GOOGLE_GENAI_TEMPERATURE=float. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 
GOOGLE_GENAI_TOP_P=float. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 
GOOGLE_GENAI_TOP_K=int. optional. learn from https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values . if left empty, the default value is defined at noviirnawati/config/sdk_configuration.py 

AI_ANALYSIS_SAVED_AS_MARKDOWN=bool. optional. true to save markdown of generated content into a markdown file locally. if left empty, the default value is False, defined at noviirnawati/config/base_configuration.py 
OUTPUT_FILENAME_API_DETAILS=string. optional. file name of which web data scraping result. file will be save as output_[file_name]-[spotify_playlist_id]-[yymmdd].json
OUTPUT_FILENAME_SONGS_DETAILS=string. optional. file name of which cleaned data result. file will be save as output_[file_name]-[spotify_playlist_id]-[yymmdd].json
```

A sample populated with example data types:

```dotenv
# Spotify API credentials
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here

# Google AI credentials
GOOGLE_CLOUD_API_KEY=API key, get yours from https://aistudio.google.com/app/api-keys
GOOGLE_GENAI_MODEL_TYPE=gemini-2.0-flash-001

GOOGLE_GENAI_SYSTEM_INSTRUCTION=You are a Relationship Pop Culture Analyst. Your primary function is to identify and objectively analyze potential behavioral or personality 'dating red flags' associated with a music listener, based solely on the lyrical themes, dominant mood, and artist personas present in the provided playlist data. Strict Output Rule: You MUST return your complete analysis with MARKDOWN format, with sections: Summary: A single paragraph high-level summary of the findings. Red Flags: Flag Category: e.g., Emotional Volatility, Commitment Avoidance, Materialism. Reasoning: A brief explanation of why this category was chosen, citing the lyrical themes or mood. Supporting Songs: Songs and artist to support the result
GOOGLE_GENAI_BASE_PROMPT=Perform a dating red flag analysis on the following music playlist. The playlist data is provided as a semicolon-separated list in the format (Song Title - Artist). Use the themes and moods of the songs to infer potential personality concerns. Strictly follow the MARKDOWN format defined in your instructions.
GOOGLE_GENAI_TEMPERATURE=0.7
GOOGLE_GENAI_TOP_P=0.6
GOOGLE_GENAI_TOP_K=30

AI_ANALYSIS_SAVED_AS_MARKDOWN=True
OUTPUT_FILENAME_API_DETAILS=api_details
OUTPUT_FILENAME_SONGS_DETAILS=songs_details
```

-----

## **Future Roadmap (Post-MVP)**
The immediate roadmap focuses on expanding data context and analysis depth, building directly on the successful MVP foundation:
* **Trying New AI Voices**: Looking into other GenAI providers (especially those with a great free tier!) to see how
  their models analyze music and if we can get a different "vibe" for the analysis.
* **Deeper Data Dive**: I'll be trying to scrape more detailed metrics like Genre, BPM, and Mood from the network
  traffic. More data means the AI can give even spicier and more nuanced "red flag" assessments!
* **Visualizing the Vibe**:Exploring suitable data visualization based on the collected playlist data.
* A revised overall application flow:
  ```
  Spotify Playlist ⟶ Data Scraping ⟶ Data Cleaning ⟶ Feature Extraction ⟶ AI Model ⟶ Analysis Output ⟶ Data Visualization
  ```
* Feature extraction might focus on playlist-level insights, such as:
    * Number of songs in a playlist
    * Min (Oldest), Max (Latest), Most Common Release Year to get era preference.
    * Min (Shortest), Max(Longest), Average Songs Duration to get duration preference.
    * Artist distribution & diversity, Top 3 Artists to see if the user is loyal to their favorite artists or explores
      many.
    * Genre distribution & diversity, Top 3 Genres to see if the user has a comfort genre or explores many.
    * BPM distribution & diversity, Top 3 BPM to see if the user prefers a faster or slower tempo.
    * Mood distribution & diversity, Top 3 Moods to see how consistent their moods are.
    * ...and more.
    * If those data points are available to scrape from Spotify's Web UI, I'll definitely try to integrate them.
      Otherwise, these ideas may become optional features should I decide to explore the Spotify API later on.