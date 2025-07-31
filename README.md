
# DDGem 💎

[](https://opensource.org/licenses/MIT)

**DDGem** is a simple and robust Python library that "connects" Google's language models to the internet. It uses DuckDuckGo search to find up-to-date information and provide verified, more accurate answers based on it.

The main advantage is that the base version uses the free **`gemma-3n-e4-it`** model by default, allowing you to get enhanced, fact-checked, and structured answers **completely for free**.

## Key Features ✨

  * **Fact-Checking:** Enriches model responses with real-time information from the web to avoid hallucinations.
  * **Structured Output:** Prompts the model to return answers in a clean JSON format, ready for use in your code.
  * **Free to Use:** Configured to work with the free `Gemma` model out of the box.
  * **Simple & Flexible:** A clean design makes the library easy to integrate into any project.

-----

## Installation 📦

This library is not yet published on PyPI. You can install it by cloning the repository from GitHub:

```bash
git clone https://github.com/your-username/ddgem.git
cd ddgem
poetry install
```

-----

## How to Use 🚀

The library is designed to be as intuitive as possible.

**1. Set up your API key:**
Create a `.env` file in your project's root directory and add your key from Google AI Studio:

```
GEMINI_API_KEY="your_api_key_here"
```

**2. Example Code:**

```python
import os
import json
from dotenv import load_dotenv
from ddgem import get_default_ddgem_client

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    ddgem = get_default_ddgem_client(api_key=api_key)
    
    query = "What is a black hole?"
    answer = ddgem.get_fact_checked_answer(query)

if __name__ == "__main__":
    main()
```

-----

## Example Response

The library returns a JSON object with the following structure:

```json
{
  "title": "Black Holes Explained",
  "article": "A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from it. It is formed when a massive star collapses at the end of its life cycle. The boundary of a black hole is called the event horizon, which marks the point of no return.",
  "key_facts": [
    "They are formed from the remnants of massive stars.",
    "The gravitational pull is so immense that not even light can escape.",
    "The center of a black hole is a gravitational singularity, a point of infinite density.",
    "Supermassive black holes are believed to exist at the center of most large galaxies, including our own."
  ]
}
```

-----

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
