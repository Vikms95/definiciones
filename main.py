from get_spanish_definition import get_spanish_definition 
from db_to_dict import db_to_dict
from anki_service import anki_request, get_request_dict
from keyboard import add_with_keyboard
# kindle needs to be connected to the laptop
def main():
    kindle_words = db_to_dict()
    anki_ids = anki_request('findCards', **{"query":"deck:spanish"})
    anki_words_info = anki_request('cardsInfo', **{"cards": anki_ids})
    anki_words = [word['fields']['Word']['value'] for word in anki_words_info]
    for [each_kindle_word] in kindle_words:
        if(each_kindle_word not in anki_words):
            word_dict = get_spanish_definition(each_kindle_word)
            request_dic = get_request_dict(**word_dict)
            anki_request('guiAddCards', **request_dic)
            add_with_keyboard()
main()


