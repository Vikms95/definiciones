from pyrae import dle
from blacklist import spanish_blacklist, append_problematic_words_to_blacklist
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def query_all_spanish_definitions(kindle_words, existing_anki_words):
    valid_words = [
        kindle_word[0] for kindle_word in kindle_words
        if kindle_word[0] and is_new_valid_word(kindle_word[0], existing_anki_words)
    ]
    
    results = []
    with ProcessPoolExecutor(max_workers=100) as executor: 
        future_to_word = {executor.submit(get_spanish_definition, word): word for word in valid_words}
        for future in as_completed(future_to_word):
            word = future_to_word[future]
            try:
                result = future.result()
                if result is not None:
                    results.append(result)
                else:
                    spanish_blacklist.append(word)
            except Exception as exc:
                spanish_blacklist.append(word)
                print('%r generated an exception: %s' % (word, exc))

    append_problematic_words_to_blacklist()
    return results
        
def is_new_valid_word(kindle_word, existing_anki_words):
    return kindle_word not in existing_anki_words and kindle_word not in spanish_blacklist and len(kindle_word) > 1

async def get_and_filter_spanish_definition(word: str):
    result = await get_spanish_definition(word)
    
    print('hello world')
    if result is not None:
        return result
    else:
        spanish_blacklist.append(word)
        


def get_spanish_definition(word: str):
    try:
        response = dle.search_by_word(word)
        if hasattr(response, 'meta_description'):
            parts = response.meta_description.split("1.", 1)
            if len(parts) > 1:
                definition = '1.' + parts[1]
                return {"word": word, "definition": definition}
    except (IndexError, AttributeError) as e:
        print(f"An error occurred: {e}")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")
    return None
