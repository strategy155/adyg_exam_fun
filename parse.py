from lxml.html.soupparser import parse
from re import sub
text = parse('ПОЛИТИКЭР | Адыгэ Макъ.html').getroot().text_content()
with open('adyghe-unparsed-words.txt', 'r') as f:
    adyg_words = f.read().split('\n')
text = text.replace('|', ' ')
text = text.replace('I', '|')
text = sub('[^а-яА-ЯёЁ|\s]', '', text.lower())
html_words = list(filter(None,text.replace(' ', '\n').replace('\t', '').split('\n')))
adyg_set = set()
for elem in html_words:
    if elem in adyg_words:
        adyg_set.add(elem)
words_met = list(adyg_set)
with open('wordlist.txt', 'w') as fo:
    for elem in words_met:
        fo.write(elem+ '\n')