import time
import random
from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import RatelimitException

def fetch_image_url(search_term, max_retries=5, delay_seconds=1):
    retries = 0

    while retries < max_retries:
        try:
            with DDGS() as ddgs:
                results = ddgs.images(
                    keywords=search_term,
                    region='wt-wt',
                    safesearch='moderate',
                    max_results=1
                )

            if not results:
                raise Exception(f"No images found for '{search_term}'")

            # Success: return the image URL
            return results[0]['image']

        except RatelimitException:
            # If blocked: wait and retry
            retries += 1
            wait_time = delay_seconds * retries + random.uniform(0, 1)
            print(f"Rate limit hit. Waiting {wait_time:.2f} seconds before retrying ({retries}/{max_retries})...")
            time.sleep(wait_time)

    # After retries exhausted
    raise Exception(f"Failed to fetch image for '{search_term}' after {max_retries} retries due to rate limits.")

