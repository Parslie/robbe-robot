import random
import json
import os

custom_fn = "custom_quotes.json"
default_fn = "default_quotes.json"
custom_quotes = dict()
default_quotes = dict()


def add(set_id, quote):
    if set_id not in custom_quotes:
        custom_quotes[set_id] = []
    custom_quotes[set_id].append(quote)
    save()


def remove(set_id, quote_index):
    if set_id not in custom_quotes:
        raise Exception(f'There is no custom quote of type "{set_id}"!')
    elif len(custom_quotes[set_id]) < quote_index + 1:
        raise Exception(f'No custom quote of index {quote_index} exists!')

    custom_quotes[set_id].pop(quote_index)
    save()


def get(set_id):
    quotes = []
    if set_id in custom_quotes:
        quotes.extend(custom_quotes[set_id])
    if set_id in default_quotes:
        quotes.extend(default_quotes[set_id])
    
    if len(quotes) == 0:
        return None
    return random.choice(quotes)


def save():
    with open(custom_fn, 'w', encoding='utf-8') as f:
        f.write(json.dumps(custom_quotes))


def init():
    global default_quotes
    global custom_quotes

    if os.path.exists(default_fn):
        with open(default_fn, 'r', encoding='utf-8') as f:
            default_quotes = json.loads(f.read())
    if os.path.exists(custom_fn):
        with open(custom_fn, 'r', encoding='utf-8') as f:
            custom_quotes = json.loads(f.read())