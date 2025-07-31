from google import genai
import json
from .ddsearch import DDSearch
from src.ddgem.exceptions import SearchException
from google.genai import errors
import logging

logger = logging.getLogger(__name__)

class GeminiClient:
    """
    A client to interact with the Google Gemini API, using an external 
    search client to augment prompts with real-time information.
    """
    def __init__(self, search_client: DDSearch, genai_client: genai.Client):
        
        self.client = genai_client
        self.search_client = search_client


    def get_fact_checked_answer(self, query: str, 
                                model_name: str = 'gemma-3n-e4b-it') -> dict | str | None:
        
        """
        Retrieves a model's answer based on facts checked against the internet.

        This method performs a full RAG cycle:
        1. Searches the internet for context based on the user's query.
        2. Builds a complex prompt that includes the retrieved facts.
        3. Sends the prompt to the language model.
        4. Attempts to parse the response as JSON. If it fails, returns the raw text.

        Args:
            query (str): The user's question.
            model_name (str, optional): The name of the model to use for generation. 
                                        Defaults to 'gemma-3n-e4b-it'.

        Returns:
            dict | str | None: The parsed JSON response as a dictionary if successful.
                               In case of a parsing error, the raw text response.
                               Returns None in case of a complete failure.
        """

        if not query:
            raise ValueError("Query can't be None or empty.")
        
        try:
            summaries = self.search_client.get_fresh_summaries(query)
            context = '\n'.join(f"- {s}" for s in summaries)
        except SearchException as e:
            logger.error(f"\nError during search: {e}")
            context = "Couldn't get information from the internet."
        

        final_query = f"""
            Analyze the user's question based on the provided facts from the internet below.
            If your internal knowledge contradicts these facts, always give priority to the facts.
            Format the response strictly as a JSON object with the keys "title", "article", and "key_facts".
            Try to write "article" as big as possible.
            Do not add any text before or after the JSON object.
            Respond in the same language as the user's question.

            ---
            **Facts from the internet:**
            {context}
            ---
            **User's question:**
            {query}
        """

        try:
            response = self.client.models.generate_content(
                model= model_name,
                contents=final_query
            )

            cleaned_text = response.text.strip().strip('```').strip('json').strip()

            parsed_data = json.loads(cleaned_text)
            return parsed_data
        
        except errors.APIError as e:
            logger.error(f"An error occurred with the Google API: {e}")
            return None 

        except json.JSONDecodeError:
            logger.error("Failed to parse the model's response as JSON.")
            return cleaned_text

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None
        
