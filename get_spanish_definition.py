from pyrae import dle
from blacklist import spanish_blacklist, append_problematic_words_to_blacklist
from concurrent.futures import ProcessPoolExecutor, as_completed

def query_all_spanish_definitions(kindle_words, existing_anki_words):
    valid_words_info = [
        { "word": kindle_word[0], "usage": kindle_word[1] } for kindle_word in kindle_words
        if kindle_word[0] and is_new_valid_word(kindle_word[0], existing_anki_words)
    ]

    if valid_words_info is None or len(valid_words_info) == 0: 
        return None
    
    results = []
    with ProcessPoolExecutor(max_workers=100) as executor: 
        future_to_word = {
            executor.submit(get_spanish_definition, word_info['word'], word_info['usage']): word_info
        for word_info in valid_words_info
        }
        for future in as_completed(future_to_word):
            word_info = future_to_word[future]
            try:
                result = future.result()
                if result is not None:
                    results.append(result)
                else:
                    spanish_blacklist.append(word_info['word'])
            except Exception as exc:
                spanish_blacklist.append(word_info)
                print('%r generated an exception: %s' % (word_info, exc))

    append_problematic_words_to_blacklist()
    return results
        
def is_new_valid_word(kindle_word, existing_anki_words):
    return kindle_word not in existing_anki_words and kindle_word not in spanish_blacklist and len(kindle_word) > 1


def get_spanish_definition(word: str, usage: str):
    try:
        response = dle.search_by_word(word)
        if hasattr(response, 'meta_description'):
            parts = response.meta_description.split("1.", 1)
            if len(parts) > 1:
                definition = '1.' + parts[1]
                return {"word": word, "definition": definition, "usage": usage}
    except (IndexError, AttributeError) as e:
        print(f"An error occurred: {e}")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")
    return None
