import pandas
import re

from string import punctuation
from collections import Counter

import config

puncts = config.puncts
puncts_to_keep = config.puncts_to_keep
mispell_dict = config.mispell_dict

def clean_text(x):
    x = str(x)
    for punct in puncts:
        if punct in puncts_to_keep :
            x = x.replace(punct, ' {} '.format(punct))
        else:
            x = x.replace(punct, '')
    return x


def clean_numbers(x):
    x = re.sub('[0-9]{5,}', '#####', x)
    x = re.sub('[0-9]{4}', '####', x)
    x = re.sub('[0-9]{3}', '###', x)
    x = re.sub('[0-9]{2}', '##', x)
    return x


def smart_space(x):
    return re.sub(r'\s+', ' ', x)


def smart_start_space(x):
    return re.sub(r'^\s+', '', x)


def smart_end_space(x):
    return re.sub(r'\s+$', '', x)


def remove_repeated_punctuation(x):
    return re.sub(r'(([^\w\s])\2+)', 'punctuation_incistance', x)


def count_punctuation(x):
    return Counter(c for line in x for c in line if c in punctuation)


def formating_caracter_correction(x):
    data = x
    data = re.sub(r'ç|ã§', 'c', data)
    data = re.sub(r'œ', 'oe', data)
    data = re.sub(r'æ', 'ae', data)
    data = re.sub(r'ý|ÿ', 'y', data)
    data = re.sub(r'ã¼|ã»|ã¹|ú|ù|û|ü', 'u', data)
    data = re.sub(r'ã¶|ã´|ø|ó|ð|ò|ô|ö|õ', 'o', data)
    data = re.sub(r'ã®|ã¯|í|ì|î|ï', 'i', data)
    data = re.sub(r'é|è|ê|ë|ãª|ã©|ã¨|ã«', 'e', data)
    data = re.sub(r'à|á|â|ä|å', 'a', data)
    return data


def count_lower(x):
    return sum(1 for c in x if c.islower())


def count_upper(x):
    return sum(1 for c in x if c.isupper())


def to_lower(x):
    return x.lower()


def _get_mispell(mispell_dict):
    mispell_re = re.compile('(%s)' % '|'.join(mispell_dict.keys()))
    return mispell_dict, mispell_re

    
mispellings, mispellings_re = _get_mispell(mispell_dict)

    
def replace_typical_misspell(text):
    def replace(match):
        return mispellings[match.group(0)]
    return mispellings_re.sub(replace, text)


def full_cleaning(text):
    smart_end_space(
        smart_start_space(
            smart_space(
                clean_numbers(
                    clean_text(
                        remove_repeated_punctuation(
                            formating_caracter_correction(
                                replace_typical_misspell(
                                    to_lower(text)))))))))

def analysis(text):
    res = {}
    res['char_lower'] = count_lower(text)
    res['char_upper'] = count_upper(text)
    res['punct'] = count_punctuation(text)
    return res
