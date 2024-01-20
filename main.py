from db_to_dict import db_to_dict
from anki_service import anki_request, get_request_dict
from keyboard import add_with_keyboard
from get_spanish_definition import query_all_spanish_definitions
from blacklist import load_spanish_blacklist,spanish_blacklist

def main():
    # kindle needs to be connected to the laptop
    kindle_words = db_to_dict()
    load_spanish_blacklist()
    anki_ids = anki_request('findCards', **{"query":"deck:spanish"})
    anki_words_info = anki_request('cardsInfo', **{"cards": anki_ids})
    existing_anki_words = [word['fields']['Word']['value'] for word in anki_words_info]
    words_dict = query_all_spanish_definitions(kindle_words, existing_anki_words)
    print(words_dict)
    print(spanish_blacklist)
    # for dict_idx in words_dict:
    #     if dict_idx is not None:
    #         request_dic = get_request_dict(**dict_idx)
    #         anki_request('guiAddCards', **request_dic)
    #         add_with_keyboard()
main()





# TODO: join usage columns
# TODO: better way to add?
# TODO: add english words to different deck