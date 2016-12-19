import re

filename = 'rus_nouns_parsed.txt'

with open(filename, 'r') as f:
    all_strs = f.read().split('\n')
diff = 0
with open('sql.txt', 'w') as fo:
    for elem in all_strs:
        diff+=1
        without_vars = re.sub('\((.*?)\)','', elem)
        try:
            all_vars = without_vars.split('{')[1].split('|')
        except IndexError:
            diff-=1
            continue
        all_lemmas = []
        for var in all_vars:
            all_lemmas.append(var.split('=')[0])
            dif_lemmas = list(set(all_lemmas))
        wordform = without_vars.split('{')[0]
        for lemma in dif_lemmas:
            fo.write('INSERT INTO rus_words (id, wordform, lemma)' + '\n')
            fo.write('VALUES (' + str(diff) + ', ' + wordform + ', ' + lemma + ')' + '\n')
            diff+=1
        diff-=1