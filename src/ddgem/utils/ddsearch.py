from ddgs import DDGS
from ddgs.exceptions import DDGSException
from src.ddgem.exceptions import SearchException

class DDSearch:
    """A wrapper for the DuckDuckGo Search API client."""

    #need to add DI later
    def __init__(self):
        self.ddgs = DDGS(timeout=15)

    def get_fresh_summaries(self, query: str, max_results: int = 7) -> list[str]:

        """
        Performs a search and returns a list of result summaries (bodies).

        Args:
            query: The search query string.
            max_results: The maximum number of results to return.

        Returns:
            A list of strings, where each string is a search result summary.

        Raises:
            SearchException: If an error occurs during the search.
        """

        if not query:
            raise SearchException('Query is empty, sorry')
        
        try:
            results = self.ddgs.text(query, max_results=max_results)
            summaries = [r['body'] for r in results if 'body' in r]
            return summaries
                
        except DDGSException as e:
            raise SearchException(f'Error during DDG search: {e}')
        
        except Exception as e:
            raise SearchException(f"Unexpected error during search: {e}")
        
        