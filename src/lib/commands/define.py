import json

import requests


def define(args, **kwargs):
    word = args[0].replace(' ', '%20')
    word_url = 'http://api.urbandictionary.com/v0/define?term=' + word
    word_resp = requests.get(url=word_url)
    translated_word = json.loads(word_resp.content)
    found_word = translated_word['list'][0]['word']
    definition = translated_word['list'][0]['definition']
    example = translated_word['list'][0]['example']
    intended_output = "Definition for {}: {}. Example: {}".format(
        found_word, definition, example)

    return intended_output
