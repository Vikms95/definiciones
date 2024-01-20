from get_spanish_definition import get_spanish_definition 
from db_to_dict import db_to_dict
from anki_service import anki_request, get_request_dict
from keyboard import add_with_keyboard
import asyncio


def main():
    # kindle needs to be connected to the laptop
    kindle_words = db_to_dict()
    anki_ids = anki_request('findCards', **{"query":"deck:spanish"})
    anki_words_info = anki_request('cardsInfo', **{"cards": anki_ids})
    anki_words = [word['fields']['Word']['value'] for word in anki_words_info]
    for [kindle_word] in kindle_words:
        if(kindle_word not in anki_words):
            # 1.
            word_dict = get_spanish_definition(kindle_word)
            # 
            print(word_dict )
            # request_dic = get_request_dict(**word_dict)
            # anki_request('guiAddCards', **request_dic)
            # add_with_keyboard()
main()


# TODO: join usage columns
# TODO: better way to add?
# TODO: add english words to different deck
# TODO: 1. https://stackoverflow.com/questions/34377319/combine-awaitables-like-promise-all