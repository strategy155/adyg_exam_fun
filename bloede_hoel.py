import re

filename = 'rus_nouns_parsed.txt'

with open(filename, 'r') as f:
    all_strs = f.read().split('\n')
with open('sql.txt', 'w') as fo:
    for idx,elem in enumerate(all_strs):
        without_vars = re.sub('\((.*?)\)','', elem)
        try:
            all_vars = without_vars.split('{')[1].split('|')
        except IndexError:
            idx-=1
            continue
        all_lemmas = []
        for var in all_vars:
            all_lemmas.append(var.split('=')[0])
            dif_lemmas = list(set(all_lemmas))
        wordform = without_vars.split('{')[0]
        for idx2, lemma in enumerate(dif_lemmas):
            true_idx = idx+idx2 - 1
            fo.write('INSERT INTO rus_words (id, wordform, lemma)' + '\n')
            fo.write('VALUES (' + str(true_idx) + ', ' + wordform + ', ' + lemma + ')' + '\n')