# **Project: Spotify Playlist "Dating Red Flag" Analysis**

-----

## **Summary**

This project analyzes a user's Spotify playlist to generate a fun and entertaining **"dating red flag"** personality analysis. It's a lighthearted tool designed for entertainment purposes only and should not be used for any psychological or diagnostic evaluations.

The core idea is to:

  * Analyze songs from a public Spotify playlist.
  * Generate a personality analysis focused on potential **"dating red flags"**.
  * Utilize Generative AI (GenAI) for text generation.

-----

## **Technology Stack**

  * **Generative AI:** The project uses the Google **Vertex AI API SDK** to explore and implement GenAI capabilities.
  * **Web Scraping:** **Selenium** is used for web automation to scrape song and artist data from a Spotify playlist URL by listening to network traffic.
  * **Python 3:** The entire application is built using Python 3.

-----

## **How It Works**

This is the overall flow of the application:

```
Spotify Playlist ⟶ Data Scraping ⟶ Data Cleaning ⟶ AI Model ⟶ Analysis Output
```

1.  The application is run with a single command-line argument: the URL of a public Spotify playlist.
2.  **Selenium** automates the web browser to navigate to the provided URL.
3.  The application listens to the network traffic and extracts a list of songs and artists from the web UI elements.
4.  The extracted data, along with specific prompts and system instructions, is sent to the GenAI model.
5.  The AI model, accessed via the Vertex AI API SDK, generates the personality analysis based on the provided data and instructions.
6.  The final AI-generated response is saved as a Markdown file, with the filename automatically generated in the format `result-[spotify_playlist_id]-[yymmdd].md`.
      * **Example:** If the playlist URL is `https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq`, and the analysis is run on December 31, 2025, the output file will be named `result-7wARwuyCiPRMURGmh6xTLq-251231.md`.

-----

## **Requirements**

  * **Python 3**
  * **Google Vertex AI API Key and Authentication:** All required environment variables are listed in the `Environment Variables` section.
  * **Python Modules:** All required modules are listed in the `requirements.txt` file.

***Note:*** *Further details on the specific Python dependencies and the chosen AI platform (Google Vertex AI) will be added in a future update.*

-----

## **How to Run**

1.  Navigate to the project directory in your terminal: `.../spotify-playlist-dating-redflag-analysis`.

2.  Run the application as a Python module using the following command:

    ```bash
    python -m noviirnawati.main [your_public_spotify_link]
    ```

3.  Alternatively, if you are using PyCharm, you can use the pre-configured run configuration file located at `spotify-playlist-dating-redflag-analysis/.run`. You may need to edit the configuration to match your project's local path.

-----

## **Project Structure**

  * `.run/`: PyCharm run configuration files.
  * `docs/`: Additional documentation (if necessary).
  * `noviirnawati/`: The main Python package.
      * `constant/`: Contains modules with constant classes and immutable variables.
      * `env/`: A directory for storing credentials. This directory is not uploaded to the repository.
      * `helper/`: Contains modules that support the logical processes of the project.
      * `model/`: Contains modules with data definition classes.
      * `output/`: Contains generated output files from the application, such as the analysis report.
      * `sdk/`: Contains modules for implementing the Vertex AI API SDK and its configurations.
      * `web_scraper/`: Contains modules for performing data scraping from the provided URL.
  * `tests/`: A package for unit tests.
      * ***Note:*** *Unit testing is planned for the future, after the Generative AI exploration is complete.*

-----

## **Configuration & Environment Variables**

This project relies on several environment variables for configuration. The sample below is populated with the data type corresponding to each environment variable key.

```dotenv
GOOGLE_CLOUD_PROJECT=string
GOOGLE_CLOUD_LOCATION=string
GOOGLE_GENAI_USE_VERTEXAI=bool
GOOGLE_GENAI_API_VERSION=string
GOOGLE_GENAI_MODEL_TYPE=string

GOOGLE_GENAI_SYSTEM_INSTRUCTION=string
GOOGLE_GENAI_TEMPERATURE=float
GOOGLE_GENAI_TOP_P=float
GOOGLE_GENAI_TOP_K=int

AI_ANALYSIS_SAVED_AS_MARKDOWN=bool
DATA_SCRAPING_SAVE_API_DETAILS=bool
DATA_SCRAPING_SAVE_SONGS_DETAILS=bool

OUTPUT_FILENAME_API_DETAILS=string
OUTPUT_FILENAME_SONGS_DETAILS=string
```

-----

## **Future Updates**

Future plans for this project include:

  * Exploring deeper data collection, such as genre, BPM, and mood, if available from the Spotify API, and integrating it with the AI model for a broader response.
  * Exploring suitable data visualization based on the collected playlist data.
  * A revised overall application flow:
    ```
    Spotify Playlist ⟶ Data Scraping ⟶ Data Cleaning ⟶ Feature Extraction ⟶ AI Model ⟶ Analysis Output ⟶ Data Visualization
    ```
  * Feature extraction might focus on playlist-level insights, such as:
      * Number of songs in a playlist
      * Min (Oldest), Max (Latest), Most Common Release Year to get era preference.
      * Min (Shortest), Max(Longest), Average Songs Duration to get duration preference.
      * Artist distribution & diversity, Top 3 Artists to see if the user is loyal to their favorite artists or explores many.
      * Genre distribution & diversity, Top 3 Genres to see if the user has a comfort genre or explores many.
      * BPM distribution & diversity, Top 3 BPM to see if the user prefers a faster or slower tempo.
      * Mood distribution & diversity, Top 3 Moods to see how consistent their moods are.
      * ...and more.