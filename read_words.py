from sqlalchemy.exc import IntegrityError

from database import Word, get_word


def read_words(filename):
    file = open(filename,'r')
    print('creating words from %s'%filename)
    for line in file:
        word = Word(word=line,anagram=''.join(sorted(list(line[0:len(line)-1]))))
        try:
            word.save()
        except IntegrityError as e:
            pass
        # print(word)


# read_words('dehkhoda.txt')
# read_words('moin.txt')
# read_words('wiki.txt')
word = input()
word = list(word)
print(get_word(''.join(sorted(list(word)))).all())