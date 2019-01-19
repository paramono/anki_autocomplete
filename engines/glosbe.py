try:
    import urlparse
    from urllib import urlencode
except ImportError:  # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

import requests


class AutocompleteGlosbe(object):
    url = 'https://glosbe.com/ajax/phrasesAutosuggest'
    # '?from={from}&dest={to}&phrase={text}'

    @classmethod
    def query(cls, text, **kwargs):
        '''
        required params: from dest phrase
        returns list of strings
        '''
        params = {'from': 'en', 'dest': 'ru', 'phrase': text, 'tm': True}
        r = requests.get(cls.url, params=params)
        if not r.status_code == 200:
            # showInfo('Request failed: %s' % r.status_code)
            raise ValueError
        return r.json()
