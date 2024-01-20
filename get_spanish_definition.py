from pyrae import dle


def get_spanish_definition(word: str):
    try:
        response = dle.search_by_word(word)
        return {"word": word, "definition": '1.' + response.__str__().split("1.",1)[1]}
    except Exception as e:
        return f'Definición no encontrada: {e}'