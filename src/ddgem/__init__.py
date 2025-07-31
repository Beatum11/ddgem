from src.ddgem.utils.ddsearch import DDSearch
from src.ddgem.utils.gem import GeminiClient
from src.ddgem.exceptions import SearchException
from google import genai

__all__ = ["DDSearch", "GeminiClient", "SearchException"]

#need to think about this later
def get_default_ddgem_client(api_key: str):

    if not api_key:
        raise ValueError('Need to provide api_key')
    
    dd_search = DDSearch()
    genai_client = genai.Client(api_key=api_key)

    return GeminiClient(search_client=dd_search, genai_client=genai_client)
    