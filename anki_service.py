import json
import urllib.request

url = "http://127.0.0.1:8765"

def anki_request(action,**params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request(url, requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

def get_deck_words():
    requestJson = json.dumps(request('findCards', **{"deck:Spanish"})).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request(url, requestJson)))



def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def get_request_dict(**word_dict):
    return {
        "note": {
            "deckName": "Spanish",
            "modelName": "Reverse",
            "fields": {
                "Word": word_dict['word'],
                "Definition": word_dict['definition'],
                "Usage": "aaa"
            },
        }
    }
    