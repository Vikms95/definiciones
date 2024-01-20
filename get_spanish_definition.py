from pyrae import dle
import asyncio
from blacklist import spanish_blacklist

def query_all_spanish_definitions(kindle_words, existing_anki_words):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        results = loop.run_until_complete(await_all_spanish_definitions(kindle_words, existing_anki_words))
        return results
    finally:
            loop.close()
        

async def await_all_spanish_definitions(kindle_words, existing_anki_words):
    # Filter kindle_words to include only those that are not in anki_words and are valid
    valid_words = [
        kindle_word[0] for kindle_word in kindle_words
        if kindle_word[0] and is_new_valid_word(kindle_word[0], existing_anki_words)
    ]
    
    # Create a list of coroutines for each valid word
    coroutines = [get_and_filter_spanish_definition(word) for word in valid_words]
    
    # Execute the coroutines concurrently and wait for all to complete
    results = await asyncio.gather(*coroutines)
    return results

def is_new_valid_word(kindle_word, existing_anki_words):
    return kindle_word not in existing_anki_words and kindle_word not in spanish_blacklist and len(kindle_word) > 1

async def get_and_filter_spanish_definition(word: str):
    # Call the original function
    result = await get_spanish_definition(word)
    
    # Return the result only if it's not None
    if result is not None:
        return result


async def get_spanish_definition(word: str):
    try:
        response = dle.search_by_word(word)
        if hasattr(response, 'meta_description'):
            parts = response.meta_description.split("1.", 1)
            if len(parts) > 1:
                definition = '1.' + parts[1]
                return {"word": word, "definition": definition}
        else:
            spanish_blacklist.insert(word)
    except (IndexError, AttributeError) as e:
        # Optionally, log or print the error message for debugging
        print(f"An error occurred: {e}")