from pyrae import dle
import asyncio
from blacklist import spanish_blacklist, append_problematic_words_to_blacklist

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
    valid_words = [
        kindle_word[0] for kindle_word in kindle_words
        if kindle_word[0] and is_new_valid_word(kindle_word[0], existing_anki_words)
    ]
    
    coroutines = [get_and_filter_spanish_definition(word) for word in valid_words]
    
    results = await asyncio.gather(*coroutines)
    append_problematic_words_to_blacklist()
    return results

def is_new_valid_word(kindle_word, existing_anki_words):
    return kindle_word not in existing_anki_words and kindle_word not in spanish_blacklist and len(kindle_word) > 1

async def get_and_filter_spanish_definition(word: str):
    result = await get_spanish_definition(word)
    
    if result is not None:
        return result
    else:
        spanish_blacklist.append(word)
        


async def get_spanish_definition(word: str):
    try:
        response = dle.search_by_word(word)
        if hasattr(response, 'meta_description'):
            parts = response.meta_description.split("1.", 1)
            if len(parts) > 1:
                definition = '1.' + parts[1]
                return {"word": word, "definition": definition}
    except (IndexError, AttributeError) as e:
        print(f"An error occurred: {e}")