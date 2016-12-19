import os
def generate_mystemmed_file(filename):
    os.system("/Users/gaurwaithmelui/PycharmProjects/exam/mystem" + ' -nigw ' + filename  + ' ' + os.path.splitext(filename)[0] + '_parsed.txt')

with open('adyghe-unparsed-words_parsed.txt', 'r') as f:
    words_parsed =  f.read().split('\n')
for idx, elem in enumerate(words_parsed):
    if elem.endswith('??}'):
        words_parsed[idx]=''
words_parsed_cleaned = list(filter(None, words_parsed))
all_words = []
for elem in words_parsed_cleaned:
    if '=S' in elem and 'ед|им' in elem:
        all_words.append(elem.split('{')[0])
with open('rus_nouns.txt' ,'w') as fo:
    for elem in set(all_words):
        fo.write(elem+'\n')