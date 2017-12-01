#!/usr/bin/env python

import json
import urllib2
from bs4 import BeautifulSoup

URL = 'https://www.merriam-webster.com/word-of-the-day'

class WordOfTheDay:
    def __init__(self):
        pass

    def jsonize(self, word, meaning):
        return json.dumps({ 'word': word[0], 'meaning': meaning[0] })

    def get_wod(self):
        content = urllib2.urlopen(URL).read()
        soup = BeautifulSoup(content, "lxml")
        words = []
        meanings = []

        for div in soup.findAll('div', attrs={'class': 'word-and-pronunciation'}):
            word = div.find('h1')
            words.append(word.text.strip())

        for div in soup.findAll('div', attrs={'class': 'wod-definition-container'}):
            meaning = div.find('p')
            meanings.append(meaning.text.strip())

        return self.jsonize(words, meanings)
