from pyrae import dle


def get_spanish_definition(word: str):
    try:
        response = dle.search_by_word(word)
        if hasattr(response, 'meta_description'):
            parts = response.meta_description.split("1.", 1)
            if len(parts) > 1:
                definition = '1.' + parts[1]
                return {"word": word, "definition": definition}
        return None  # Return None if the correct format isn't found
    except (IndexError, AttributeError) as e:
        # Optionally, log or print the error message for debugging
        # print(f"An error occurred: {e}")
        return None