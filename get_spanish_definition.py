import pandas as pd
import pytz
from datetime import datetime
from pyrae import dle
from add_definition_to_anki import add_to_anki

# https://foosoft.net/projects/anki-connect/
# TODO: import the vocab.db file from the Kindle directory and copy it converted into .xlsx or csv
# TODO: 
# TODO: copy the rows that were found   
# TODO: create two .xlsx, and attach the words on one of them depending on if they were found on the english or spanish api


def get_spanish_definition(word: str):
    try:
        response = dle.search_by_word(word)
        definition = '1.' + response.__str__().split("1.",1)[1]
        return definition
    except Exception as e:
        return f'Definición no encontrada: {e}'


args = {
    "card": 13230239,
    "keys": ['flags', 'odue'],
    "newValues": ['1', '-100']
}

result = add_to_anki('guiAddCards', **{"decks": "Spanish"})
print(result)

# words_df = pd.read_excel(file_path)

#* copy to excel
# last_col_index = len(words_df.columns)
# new_col_name = 'Definicion'
# words_df.insert(last_col_index, new_col_name, words_df['word'].apply(get_spanish_definition))
# words_df.to_csv(file_path, index=False)


